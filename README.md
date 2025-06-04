# HBM-schemas-001: CSV to JSON Converter for Screen Templates

## Project Overview

This project is a specialized CSV to JSON converter designed for screen template generation. It transforms structured CSV data into a standardized JSON format that defines screen templates with their components, validations, and relationships.

### Key Features
- Converts CSV files to structured JSON screen templates
- Handles multiple component types (inputs, selectors, etc.)
- Supports complex component hierarchies
- Validates output against a predefined schema
- Flexible row selection for processing specific data

### Project Structure
```
.
├── excel_to_json_converter.py  # Main conversion script
├── validate_json.py           # JSON validation script
├── screen_schema.json         # Validation schema
├── requirements.txt           # Python dependencies
├── csv-to-convert/           # Directory for input CSV files
│   └── .gitkeep             # Keeps directory in git
├── json/                     # Directory for output JSON files
│   └── .gitkeep             # Keeps directory in git
└── README.md                 # This documentation
```

### How It Works

1. **Input Processing**
   - Reads CSV files from the `csv-to-convert` directory
   - Supports flexible row selection (all rows, range, specific indices, or IDs)
   - Validates required fields and data structure

2. **Component Mapping**
   - Maps CSV columns to JSON fields using predefined mappings
   - Handles component type conversion (e.g., "Choice" → "select_single_cards")
   - Processes component names and relationships

3. **JSON Generation**
   - Creates a new timestamped output directory under `json/`
   - Generates unique IDs for components
   - Maintains component hierarchy and relationships
   - Ensures consistent field ordering

4. **Validation**
   - Validates generated JSON against schema
   - Ensures required fields are present
   - Checks component structure and relationships

### Project Logic

The project follows these key principles:

1. **Component Type Mapping**
   - Inputs: text boxes, number fields, etc.
   - Selectors: cards, dropdowns, etc.
   - Each type has specific validation and structure requirements

2. **Component Hierarchy**
   - Parent components can have children (e.g., select cards)
   - Children inherit properties from parents
   - Maintains proper relationships and dependencies

3. **Data Validation**
   - Required fields must be present
   - Component types must be valid
   - Relationships must be properly structured

4. **Flexible Processing**
   - Can process all rows or specific selections
   - Supports different input formats
   - Maintains data integrity throughout conversion

## Table of Contents
1. [General Description](#general-description)
2. [File Structure](#file-structure)
3. [Required vs Optional Fields](#required-vs-optional-fields)
4. [CSV Column Mapping](#csv-column-mapping)
5. [Manual Fields](#manual-fields)
6. [Component Structure](#component-structure)
7. [Examples](#examples)

## General Description

This project converts CSV files to JSON format for screen templates. The main script `excel_to_json_converter.py` handles the conversion, while `validate_json.py` validates the generated JSON files against a schema.

## File Structure

```
.
├── excel_to_json_converter.py  # Main conversion script
├── validate_json.py           # JSON validation script
├── screen_schema.json         # Validation schema
├── docs/                      # Directory containing CSV files
└── json/                      # Directory for generated JSON files
```

## Required vs Optional Fields

### Required Fields
The following fields must always be present in the JSON:
- `screen_template_id`
- `name`
- `title`
- `label`
- `description`
- `components` (minimum: `id`, `component_type`, `name`)

### Optional Fields
The following fields can be missing or left empty:
- `state` (default: `"draft"`)
- `stage`
- `section`
- `scope`
- `tips`
- `tip_links`
- `small_print`
- `is_required` (default: `false`)
- `is_private` (default: `false`)
- `is_editable` (default: `true`)
- `internal`

## CSV Column Mapping

### Used Columns
| JSON Field | CSV Column | Notes |
|------------|------------|-------|
| screen_template_id | Screen_ID | Unique screen ID |
| name | Screen Name | Internal name |
| state | Stage | Screen state |
| title | Title | Visible title |
| label | Label | Short label |
| description | Description | Detailed description |
| component_type | Component type | Component type |
| component_name | Component(s) Name(s) | Component name |
| options | Options | Available options |
| validation | Data Format | Validation rules |
| default_value | Default Value | Default value |
| min_value | Hard Min / Soft Min | Minimum value |
| max_value | Soft Max / Hard Max | Maximum value |
| conditional_navigation | Conditional Nav (Linear) | Conditional navigation |
| tips | Tips | Help text |
| small_print | Small Print | Small print text |
| internal_reference | References | Internal references |
| scope | Scope | Application scope |
| section | Section | Thematic section |
| tip_links | Tip Link 1 - Label : URL, Tip Link 2 - Label : URL | Help links (array) |

### Ignored Columns
- Old Screen ID
- JSON filename
- JSON Review 1
- Review 1 Notes
- Arturo To Do
- Global Variable(s)
- Source
- Notes
- Data Transformation
- Appearance on RPA
- Appearance on Other Form
- Help Topic
- Help Context
- Additional Terms & Conditions
- Conditional Nav (Non-Linear)

## Manual Fields

The following fields are not in the CSV and must be added manually or left with default values:

| Field | Default Value | Notes |
|-------|---------------|-------|
| state | `"draft"` | Initial screen state |
| is_required | `false` | Whether the screen is required |
| is_private | `false` | Whether the screen is private |
| is_editable | `true` | Whether the screen is editable |
| internal | `{}` | Internal references and notes |

### Component Manual Fields
| Field | Default Value | Notes |
|-------|---------------|-------|
| id | Generate UUID | Unique identifier |
| is_array | `false` | Whether it's an array of values |
| is_private | `false` | Whether the component is private |
| is_editable | `true` | Whether the component is editable |
| is_required | `false` | Whether the component is required |
| is_visible | `true` | Whether the component is visible |
| default_value | `null` | Default value |
| value | `null` | Current value |
| suggested | `null` | Suggestions |
| validation | `null` | Validation rules |
| formatting | `null` | Formatting rules |
| tooltip | `null` | Help text |
| fields | `[]` | Additional fields |
| logic | `[]` | Logic rules |
| children | `[]` | Subcomponents |

## Component Structure

Each component in the JSON must have the following minimum structure:

```json
{
  "id": "uuid",
  "component_type": "type",
  "name": "name",
  "is_array": false,
  "is_private": false,
  "is_editable": true,
  "is_required": false,
  "is_visible": true,
  "default_value": null,
  "value": null,
  "suggested": null,
  "validation": null,
  "formatting": null,
  "tooltip": null,
  "fields": [],
  "logic": [],
  "children": []
}
```

## Examples

### Complete JSON Example
```json
{
  "screen_template_id": "uuid",
  "name": "screen_name",
  "state": "draft",
  "title": "Screen Title",
  "label": "Label",
  "description": "Detailed description",
  "stage": "basics",
  "section": "funds_and_financing",
  "scope": {},
  "tips": "Help text",
  "tip_links": {},
  "small_print": "",
  "is_required": false,
  "is_private": false,
  "is_editable": true,
  "internal": {},
  "components": {
    "component1": {
      "id": "uuid",
      "component_type": "input_text_line",
      "name": "component_name",
      "is_array": false,
      "is_private": false,
      "is_editable": true,
      "is_required": false,
      "is_visible": true,
      "default_value": null,
      "value": null,
      "suggested": null,
      "validation": null,
      "formatting": null,
      "tooltip": null,
      "fields": [],
      "logic": [],
      "children": []
    }
  }
}
```

## Getting Started

### Prerequisites
- Python 3.x
- Required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### First Time Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. The required directories are already included in the repository:
   - `csv-to-convert/`: Place your CSV files here
   - `json/`: Generated JSON files will be stored here

3. Place your CSV file in the `csv-to-convert` directory
   - The CSV should follow the structure described in [CSV Column Mapping](#csv-column-mapping)
   - Make sure the CSV has all required fields

4. Configure row selection (optional):
   - Open `excel_to_json_converter.py`
   - Modify the `ROW_SELECTION_MODE` variable:
     - `'all'`: Process all rows
     - `'range'`: Process a range of rows (set `ROW_RANGE`)
     - `'indices'`: Process specific indices (set `ROW_INDICES`)
     - `'ids'`: Process specific Screen_IDs (set `ROW_IDS`)

5. Run the converter:
   ```bash
   python excel_to_json_converter.py
   ```

6. Check the output:
   - JSON files will be generated in a timestamped directory under `json/`
   - Each file will be named with its `screen_template_id`

### Troubleshooting
- If you get a "No CSV files found" error, check that your file is in the `csv-to-convert` directory
- If validation fails, check that your CSV has all required fields
- If component types are not mapping correctly, verify the component type in your CSV matches the supported types

### Common Issues
1. **Missing Required Fields**: Ensure your CSV has all required fields listed in [Required Fields](#required-fields)
2. **Invalid Component Types**: Check that component types match the supported types in [Component Type Mapping](#component-type-mapping)
3. **File Location**: Make sure your CSV is in the correct directory (`csv-to-convert`)
4. **CSV Format**: Ensure your CSV is properly formatted with headers and no BOM characters 