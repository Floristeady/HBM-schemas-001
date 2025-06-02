# Data Mapping Documentation

## Overview
This document outlines the mapping between client-provided data and the required JSON format for screen templates.

## Base JSON Structure
```json
{
  "screen_template_id": "Generated UUID",
  "name": "template_name",
  "state": "draft",
  "title": "template title",
  "label": "template label",
  "description": "template description",
  "stage": "template stage",
  "section": "template section",
  "scope": {
    // Specific scope variables
  },
  "components": {
    // Specific components
  }
}
```

## Component Type Mapping

### Selection Components
| CSV Type | JSON Type | Special Properties |
|----------|-----------|-------------------|
| select_single_cards | select_single_cards | - options: Array of options with id, label, value |
| select_card | select_card | - id, label, value, icon (optional) |
| select_single_dropdown | select_single_dropdown | - options: Array of options with id, label, value |
| select_option | select_option | - id, label, value |

### Text Input Components
| CSV Type | JSON Type | Special Properties |
|----------|-----------|-------------------|
| input_text_line | input_text_line | - validation: Validation rules, max_length |
| input_text_area | input_text_area | - validation: Validation rules, max_length, rows |
| input_email | input_email | - validation: Email format validation |

### Numeric Input Components
| CSV Type | JSON Type | Special Properties |
|----------|-----------|-------------------|
| input_number | input_number | - validation: min, max, step |
| input_currency | input_currency | - validation: min, max, currency_code |
| input_percentage | input_percentage | - validation: min, max, step |

### Date and Time Components
| CSV Type | JSON Type | Special Properties |
|----------|-----------|-------------------|
| pick_date_time | pick_date_time | - format: Date/time format, min_date, max_date |

### File Components
| CSV Type | JSON Type | Special Properties |
|----------|-----------|-------------------|
| pick_file | pick_file | - accepted_types: Array of MIME types, max_size |

### Overlay Components
| CSV Type | JSON Type | Special Properties |
|----------|-----------|-------------------|
| input_overlay | input_overlay | - fields: Array of fields, layout configuration |

## Common Properties for All Components
```json
{
  "id": "Generated UUID",
  "component_type": "component_type",
  "name": "component_name",
  "is_array": false,
  "is_private": false,
  "is_editable": false,
  "is_required": false,
  "is_visible": true,
  "default_value": null,
  "value": null,
  "suggested": null,
  "validation": {},
  "formatting": null,
  "tooltip": "",
  "fields": [],
  "logic": [],
  "children": []
}
```

## Transformation Rules
1. Each component must have a unique UUID
2. Component names must be in snake_case
3. Validations must follow the format specified in the CSV
4. Default values must be converted to the appropriate data type
5. Options in select_single_cards must include id, label, and value

## Special Considerations
1. Components can have conditional logic
2. Some components can be arrays
3. Validations can include regular expressions
4. Tooltips must be converted to plain text format

## Example Component Mappings

### Select Single Cards
```json
{
  "component_type": "select_single_cards",
  "options": [
    {
      "id": "option1",
      "label": "Option 1",
      "value": "value1"
    }
  ]
}
```

### Select Card
```json
{
  "component_type": "select_card",
  "id": "card1",
  "label": "Card 1",
  "value": "value1",
  "icon": "icon-name"
}
```

### Input Text Area
```json
{
  "component_type": "input_text_area",
  "validation": {
    "max_length": 500,
    "rows": 4
  }
}
```

### Input Currency
```json
{
  "component_type": "input_currency",
  "validation": {
    "min": 0,
    "max": 1000000,
    "currency_code": "USD"
  }
}
```

### Pick Date Time
```json
{
  "component_type": "pick_date_time",
  "format": "YYYY-MM-DD HH:mm",
  "min_date": "2024-01-01",
  "max_date": "2024-12-31"
}
```

### Input Overlay
```json
{
  "component_type": "input_overlay",
  "fields": [
    {
      "name": "field1",
      "type": "input_text_line",
      "label": "Field 1"
    }
  ],
  "layout": {
    "columns": 2,
    "spacing": "medium"
  }
}
```

## Notes
- All UUIDs should be generated using a secure random generator
- Component names should be descriptive and follow a consistent naming convention
- Validation rules should be thoroughly tested before implementation
- Default values should be validated against the component's type constraints 