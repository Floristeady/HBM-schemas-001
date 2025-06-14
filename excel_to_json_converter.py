import pandas as pd
import json
import os
import uuid
from datetime import datetime
from typing import Dict, List, Any

# Global configuration for test mode
TEST_MODE = False  # Change to False to process all rows
TEST_ROWS = 10    # Number of rows to process in test mode

# --- ROW FILTERING CONFIGURATION ---
# Options:
# - 'all': process all rows
# - 'range': process a range of rows by index (e.g., 3 to 8)
# - 'indices': process a list of specific indices
# - 'ids': process a list of specific Screen_IDs
ROW_SELECTION_MODE = 'indices'  # 'all', 'range', 'indices', 'ids'
ROW_RANGE = (3, 8)          # Only if ROW_SELECTION_MODE == 'range', includes both ends
ROW_INDICES = [12, 14, 16, 22, 31, 32, 37, 46, 68]    # Only if ROW_SELECTION_MODE == 'indices'
ROW_IDS = ['id1', 'id2']    # Only if ROW_SELECTION_MODE == 'ids'

"""
CSV to JSON Column Mapping Documentation
======================================

Columnas del CSV que se usan y su correspondencia en el JSON:
------------------------------------------------------------
- Screen_ID                → screen_template_id
- Screen Name              → name
- Stage                    → state
- Title                    → title
- Label                    → label
- Description              → description
- Component type           → component_type
- Component(s) Name(s)     → component_name
- Options                  → options
- Data Format              → validation
- Default Value            → default_value
- Hard Min / Soft Min      → min_value
- Soft Max / Hard Max      → max_value
- Conditional Nav (Linear) → conditional_navigation
- Tips                     → tips
- Small Print              → small_print
- References               → internal_reference
- Scope                    → scope
- Section                  → section
- Tip Link 1 - Label : URL y Tip Link 2 - Label : URL → tip_links (array)

Columnas que NO se usan para el JSON (pueden ser ignoradas):
------------------------------------------------------------
- Old Screen ID
- JSON filename
- JSON Review 1
- Review 1 Notes
- Arturo To Do
- Global Variable(s)
- Source (solo informativa, ayuda a identificar el tipo de componente)
- Notes
- Data Transformation (solo lógica backend)
- Appearance on RPA
- Appearance on Other Form
- Help Topic
- Help Context
- Additional Terms & Conditions
- Conditional Nav (Non-Linear)

Notas:
- Si alguna columna adicional es requerida para lógica futura, se puede agregar fácilmente al mapeo.
- Las columnas ignoradas pueden contener comentarios, instrucciones internas o metadatos no relevantes para la estructura JSON de pantallas.
"""

class ExcelToJsonConverter:
    def __init__(self, input_file: str, output_dir: str = 'json', skiprows_real_csv: bool = False):
        """
        Initialize the converter with input and output paths
        
        Args:
            input_file (str): Path to the input file (Excel or CSV)
            output_dir (str): Directory where JSON files will be saved
            skiprows_real_csv (bool): If True, skip header rows (for real CSV, not for tests)
        """
        self.input_file = input_file
        self.output_dir = output_dir
        self.skiprows_real_csv = skiprows_real_csv
        self.df = None
        
        # Create date-based subfolder
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.output_dir = os.path.join(output_dir, current_date)
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        print(f"Output directory created: {self.output_dir}")
            
        # Column mapping from CSV to JSON
        self.column_mapping = {
            'Screen_ID': 'screen_template_id',
            'Screen Name': 'name',
            'Stage': 'stage',
            'Title': 'title',
            'Label': 'label',
            'Description': 'description',
            'Component type': 'component_type',
            'Component(s) Name(s)': 'component_name',
            'Options': 'options',
            'Data Format': 'validation',
            'Default Value': 'default_value',
            'Hard Min / Soft Min': 'min_value',
            'Soft Max / Hard Max': 'max_value',
            'Conditional Nav (Linear)': 'conditional_navigation',
            'Tips': 'tips',
            'Small Print': 'small_print',
            'References': 'internal_reference',
            'Scope': 'scope',
            'Section': 'section',
            'Tip Link 1 - Label : URL': 'tip_link_1',
            'Tip Link 2 - Label : URL': 'tip_link_2'
        }
        
        # Mapeo de tipos de componentes basado en Data Format
        self.component_type_mapping = {
            # Inputs
            "Text": "input_text_line",
            "Zip Code Number": "input_text_line",
            "Dollar Amount": "input_text_line",
            "Percentage": "input_text_line",
            "Number": "input_number",
            "text box": "input_text_area",
            "input_text_area": "input_text_area",
            "input_text_line": "input_text_line",
            "input_number": "input_number",
            
            # Selectores
            "Choice": "select_single_cards",
            "Dropdown": "select_single_dropdown",
            "Selection": "select_single_cards",
            "selection": "select_single_cards",
            "select_single_cards": "select_single_cards",
            "select_single_dropdown": "select_single_dropdown",
            
            # Default
            "": "input_text_area"
        }
        
        # Only these columns are strictly required
        self.required_columns = [
            'screen_template_id',
            'name',
            'stage',
            'title',
            'label',
            'description',
            'component_type'
        ]
        
    def read_file(self) -> None:
        """Read the input file into a pandas DataFrame"""
        try:
            if self.input_file.endswith('.csv'):
                # For CSV files, skip the first line (comment) and use second line as headers
                self.df = pd.read_csv(self.input_file, skiprows=1)
                
                # --- FILTRADO FLEXIBLE DE FILAS ---
                if ROW_SELECTION_MODE == 'all':
                    print("Processing all rows")
                elif ROW_SELECTION_MODE == 'range':
                    start, end = ROW_RANGE
                    self.df = self.df.iloc[start:end+1]
                    print(f"Processing rows from index {start} to {end}")
                elif ROW_SELECTION_MODE == 'indices':
                    # Filter first by desired indices
                    self.df = self.df.iloc[ROW_INDICES]
                    print(f"Processing rows with indices: {ROW_INDICES}")
                elif ROW_SELECTION_MODE == 'ids':
                    self.df = self.df[self.df['Screen_ID'].isin(ROW_IDS)]
                    print(f"Processing rows with Screen_IDs: {ROW_IDS}")
                else:
                    print("ROW_SELECTION_MODE not recognized, processing all rows")
                
                # After filtering, remove empty rows and rows with null Screen_ID
                self.df = self.df[self.df['Screen_ID'].notna()]
                self.df = self.df.dropna(how='all')
                
                print(f"Found {len(self.df)} valid rows")
                # Rename columns according to mapping
                self.df = self.df.rename(columns=self.column_mapping)
            else:
                self.df = pd.read_excel(self.input_file)
                print(f"Successfully read file: {self.input_file}")
                self.df = self.df.rename(columns=self.column_mapping)
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            raise
            
    def validate_data(self) -> bool:
        """
        Validate the input data structure
        
        Returns:
            bool: True if validation passes, False otherwise
        """
        missing_columns = [col for col in self.required_columns if col not in self.df.columns]
        if missing_columns:
            print(f"Missing required columns: {missing_columns}")
            raise ValueError("Data validation failed: Missing required columns")
            
        print("Data validation passed")
        return True
        
    def _get_value(self, row, *keys):
        """Get value from row using multiple possible keys"""
        for key in keys:
            if key in row and pd.notna(row[key]):
                return row[key]
        return ""

    def _process_value(self, value):
        """Process value to ensure correct type (bool if 'true'/'false')"""
        if pd.isna(value):
            return None
        if isinstance(value, str):
            if value.strip().lower() == 'true':
                return True
            if value.strip().lower() == 'false':
                return False
        return value

    def _format_section_name(self, section):
        """Convert section name to snake_case format"""
        if pd.isna(section):
            return ""
        # Convert to lowercase and replace spaces/special chars with underscores
        return section.lower().replace(' & ', '_and_').replace(' ', '_')

    def _process_component_name(self, name):
        """Process component name to get the base name without options and remove 'screen_' prefix"""
        if pd.isna(name):
            return ""
        # Remove 'screen_' prefix if present
        name = name.replace('screen_', '')
        # If name contains commas, take only the first part
        if ',' in name:
            name = name.split(',')[0].strip()
        # If name ends with _yes or _no, remove that suffix
        if name.endswith('_yes') or name.endswith('_no'):
            name = name.rsplit('_', 1)[0]
        return name.strip()

    def _create_children_for_select_cards(self, component_name, options):
        """Create children structure for select cards based on options"""
        children = []
        for i, option in enumerate(options):
            option = option.strip()
            # Create child name based only on the option, without repeating the parent component name
            child_name = option.lower().replace(' ', '_')
            
            child = {
                "id": str(uuid.uuid4()),
                "component_type": "select_card",
                "name": child_name,
                "is_array": False,
                "is_private": False,
                "is_editable": True,
                "is_required": False,
                "is_visible": True,
                "default_value": i == 0,  # First option is true by default
                "value": i == 0,
                "suggested": None,
                "validation": None,
                "formatting": None,
                "tooltip": None,
                "fields": [
                    {
                        "id": str(uuid.uuid4()),
                        "name": "label",
                        "label": None,
                        "value": option
                    },
                    {
                        "id": str(uuid.uuid4()),
                        "name": "description",
                        "label": None,
                        "value": ""
                    },
                    {
                        "id": str(uuid.uuid4()),
                        "name": "image",
                        "label": None,
                        "value": f"{i+1}_{child_name}.png"
                    }
                ],
                "logic": [],
                "children": []
            }
            children.append(child)
        return children

    def _create_components(self, row):
        """Create components structure as object, not array"""
        components = {}
        component_type = self._get_value(row, 'component_type', 'Component type')
        component_name = self._get_value(row, 'component_name', 'Component(s) Name(s)')
        data_format = self._get_value(row, 'validation', 'Data Format')
        options = self._get_value(row, 'options', 'Options')
        
        if component_type and component_name:
            # Process component name
            base_name = self._process_component_name(component_name)
            component_id = str(uuid.uuid4())
            
            # Determine component type based on Component type first
            mapped_type = self.component_type_mapping.get(component_type)
            
            # If not found in Component type, try with Data Format
            if not mapped_type:
                mapped_type = self.component_type_mapping.get(data_format)
            
            # If still not found, use original type
            if not mapped_type:
                mapped_type = component_type
            
            # If it's "text box" and has no options, force to input_text_area
            if mapped_type == "text box" and not options:
                mapped_type = "input_text_area"
            
            # For inputs, default_value and value must be null
            if mapped_type.startswith('input_'):
                default_value = None
                value = None
            else:
                # For select_single_cards, default_value and value must be boolean
                if mapped_type == "select_single_cards":
                    default_value = True
                    value = True
                else:
                    default_value = self._process_value(self._get_value(row, 'default_value', 'Default Value'))
                    value = default_value
            
            # Fields we know are required and their default values
            component_obj = {
                "id": component_id,
                "component_type": mapped_type,
                "name": base_name,
                "is_array": True if mapped_type in ["select_single_cards", "select_single_dropdown"] else False,
                "is_private": False,
                "is_editable": True,
                "is_required": False,
                "is_visible": True,
                "default_value": default_value,
                "value": value,
                "suggested": None,
                "validation": {
                    "value_type": "array" if mapped_type in ["select_single_cards", "select_single_dropdown"] else "text",
                    "required": True
                },
                "formatting": [] if mapped_type.startswith('input_') else None,
                "tooltip": None,
                "fields": [],
                "logic": [],
                "children": []
            }
            
            # Add children for select_single_cards and select_single_dropdown
            if mapped_type in ["select_single_cards", "select_single_dropdown"] and options:
                options_list = [opt.strip() for opt in options.split(',')]
                if mapped_type == "select_single_cards":
                    component_obj["children"] = self._create_children_for_select_cards(base_name, options_list)
                else:  # select_single_dropdown
                    component_obj["options"] = options_list
            
            components[base_name] = component_obj
            
        return components

    def _process_scope(self, row):
        """Process scope field"""
        scope = self._get_value(row, 'scope', 'Scope')
        if scope and not pd.isna(scope):
            try:
                # Try to parse as JSON
                return json.loads(scope)
            except:
                # If not valid JSON, return empty object
                return {}
        return {}

    def _process_tip_links(self, row):
        """Process tip links into proper format"""
        tip_links = {}
        
        # Process Tip Link 1
        tip1 = self._get_value(row, 'tip_link_1', 'Tip Link 1 - Label : URL')
        if tip1 and not pd.isna(tip1):
            try:
                label, url = tip1.split(' : ')
                # Remove https:// if present
                url = url.strip().replace('https://', '').replace('http://', '')
                tip_links[label.strip()] = {
                    "label": label.strip(),
                    "url": url
                }
            except:
                pass
                
        # Process Tip Link 2
        tip2 = self._get_value(row, 'tip_link_2', 'Tip Link 2 - Label : URL')
        if tip2 and not pd.isna(tip2):
            try:
                label, url = tip2.split(' : ')
                # Remove https:// if present
                url = url.strip().replace('https://', '').replace('http://', '')
                tip_links[label.strip()] = {
                    "label": label.strip(),
                    "url": url
                }
            except:
                pass
                
        return tip_links

    def _process_validation(self, row):
        """Process validation rules"""
        validation = {
            "value_type": "text",  # Default value type
            "required": False      # Default required state
        }
        # Omitir min/max values ya que se agregarán manualmente
        return validation

    def _process_options(self, options_str):
        """Process options string into array"""
        if pd.isna(options_str):
            return []
        try:
            return [opt.strip() for opt in options_str.split(',')]
        except:
            return []

    def _check_missing_fields(self, row):
        """Check which fields are missing from the CSV"""
        missing = []
        for csv_col, json_field in self.column_mapping.items():
            if csv_col not in self.df.columns or pd.isna(row.get(csv_col, '')):
                missing.append({
                    "csv_column": csv_col,
                    "json_field": json_field,
                    "status": "missing"
                })
        return missing

    def _create_json_structure(self, row):
        """Create the JSON structure for a row, ensuring all fields are present"""
        # Accept both screen_template_id and Screen_ID
        screen_template_id = self._get_value(row, 'screen_template_id', 'Screen_ID')
        name = self._get_value(row, 'name', 'Screen Name')
        stage = self._get_value(row, 'stage', 'Stage')
        title = self._get_value(row, 'title', 'Title')
        label = self._get_value(row, 'label', 'Label')
        description = self._get_value(row, 'description', 'Description')
        section = self._format_section_name(self._get_value(row, 'section', 'Section'))
        tips = self._get_value(row, 'tips', 'Tips')
        small_print = self._get_value(row, 'small_print', 'Small Print')
        internal_reference = self._get_value(row, 'internal_reference', 'References')
        scope = self._process_scope(row)
        tip_links = self._process_tip_links(row)
        
        # Fields we know are required and their default values
        json_data = {
            "screen_template_id": screen_template_id,
            "name": self._process_component_name(name),  # Remove 'screen_' prefix
            "state": "draft",  # Default value
            "title": title,
            "label": label,
            "description": description,
            "stage": stage,    # Value from CSV
            "section": section,
            "scope": scope,
            "tips": tips,
            "tip_links": tip_links,
            "small_print": small_print,
            "is_required": True,
            "is_private": False,
            "is_editable": True,
            "internal": {
                "references": internal_reference,
                "notes": ""  # Empty value for now
            },
            "components": self._create_components(row)
        }
            
        return json_data

    def convert(self) -> None:
        """Convert input data to JSON files"""
        self.read_file()
        
        if not self.validate_data():
            raise ValueError("Data validation failed")
        
        # Group by screen_template_id to combine components
        for screen_id, group in self.df.groupby('screen_template_id'):
            screen_data = self._create_json_structure(group.iloc[0])
            
            # Save to JSON file (UTF-8, ensure_ascii=False)
            output_file = os.path.join(self.output_dir, f"{screen_id}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(screen_data, f, indent=2, ensure_ascii=False)
            
            print(f"Created JSON file: {output_file}")

def main():
    # Configuration
    input_dir = "csv-to-convert"
    base_output_dir = "json"
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Directory '{input_dir}' does not exist")
        return
        
    # Find all CSV files in the input directory
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"Error: No CSV files found in '{input_dir}'")
        return
        
    print(f"Found {len(csv_files)} CSV files:")
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {file}")
    
    # Process each CSV file
    for csv_file in csv_files:
        input_file = os.path.join(input_dir, csv_file)
        print(f"\nProcessing file: {csv_file}")
        
        try:
            converter = ExcelToJsonConverter(input_file, base_output_dir, skiprows_real_csv=True)
            converter.convert()
        except Exception as e:
            print(f"Error processing {csv_file}: {str(e)}")
            continue

if __name__ == "__main__":
    main() 