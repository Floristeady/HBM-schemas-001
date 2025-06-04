# CSV to JSON Converter Documentation

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

## Usage

1. Place the CSV file in the `docs/` directory
2. Run the conversion script:
   ```bash
   python excel_to_json_converter.py
   ```
3. JSON files will be generated in the `json/` directory
4. Validate the generated files:
   ```bash
   python validate_json.py
   ``` 