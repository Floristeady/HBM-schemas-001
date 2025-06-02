# Mapping Validation Process

## Overview
This document tracks the validation process of mapping Excel data to JSON format.

## Validation Steps

### 1. Component Type Validation
For each component type in the CSV, we need to validate:
- Correct mapping to JSON component_type
- All required properties are present
- Special properties are correctly handled

### 2. Data Structure Validation
- Screen template structure
- Component hierarchy
- Required fields
- Optional fields
- Default values

### 3. Component-Specific Validation

#### Selection Components
- [ ] select_single_cards
  - [ ] Options array structure
  - [ ] ID, label, value mapping
  - [ ] Default value handling

- [ ] select_card
  - [ ] Card layout properties
  - [ ] Selection behavior

- [ ] select_single_dropdown
  - [ ] Dropdown options
  - [ ] Default selection

- [ ] select_option
  - [ ] Option properties
  - [ ] Selection state

#### Text Input Components
- [ ] input_text_line
  - [ ] Text validation rules
  - [ ] Length restrictions
  - [ ] Format requirements

- [ ] input_text_area
  - [ ] Multi-line support
  - [ ] Character limits
  - [ ] Format validation

- [ ] input_email
  - [ ] Email format validation
  - [ ] Domain restrictions

#### Numeric Input Components
- [ ] input_number
  - [ ] Number range validation
  - [ ] Decimal precision
  - [ ] Format requirements

- [ ] input_currency
  - [ ] Currency format
  - [ ] Decimal places
  - [ ] Symbol handling

- [ ] input_percentage
  - [ ] Percentage format
  - [ ] Range validation
  - [ ] Decimal precision

#### Date and Time Components
- [ ] pick_date_time
  - [ ] Date format
  - [ ] Time format
  - [ ] Range restrictions

#### File Components
- [ ] pick_file
  - [ ] File type restrictions
  - [ ] Size limits
  - [ ] Upload handling

#### Overlay Components
- [ ] input_overlay
  - [ ] Field layout
  - [ ] Component integration
  - [ ] State management

## Component Recognition Logic

### Selection Components Recognition Rules

- CSV Type: "Choice" or "Selection"

- If CSV type is "Choice" or "Selection" AND:
  - Options are 2-4 and simple (e.g., Yes/No, Seller/Buyer/Both) → select_single_cards
  - Options are more than 4 or require more context → select_single_dropdown

Examples:
- select_single_cards:
  - Yes/No selections
  - Payment type selections (Seller, Buyer, Both)
  - Loan type selections (Conventional, FHA, VA, Other)
  - Rate type selections (Fixed, Adjustable)

- select_single_dropdown:
  - Occupation type selections (Primary Residence, Secondary Residence, Investment)
  - Entity type selections (Corporation, Partnership, LLC, Other)
  - Timing selections (On Removal of All Contingencies, On a Specific Date, On Another Event/Condition)
  - Buyer type selections (Buying as Individuals, Buying as an Entity)

2. **Component Type Determination**
   - CSV Type: "check box" or "Choice" or "Selection"
     - If has 2-4 options and are simple (e.g., Yes/No, Seller/Buyer/Both) → select_single_cards
     - If has more than 4 options or require more context → select_single_dropdown
   - Value type determination:
     - For select_single_cards:
       - If has exactly 2 options → boolean value type
       - If has 3-4 options → array value type
     - For select_single_dropdown:
       - Always array value type

3. **Value Type Mapping**
   - Boolean (2 options):
     ```json
     "validation": {
       "value_type": "boolean",
       "required": true
     }
     ```
   - Array (more than 2 options):
     ```json
     "validation": {
       "value_type": "array",
       "required": true
     }
     ```

4. **Common Patterns**
   - Yes/No questions → select_single_cards with boolean
   - Type selection → select_single_cards with array
   - Single choice from list → select_single_cards with array
   - Multiple choice → select_single_cards with array (is_array: true)

5. **Error Handling**
   - If CSV type is "check box" but has more than 2 options:
     - Override to select_single_cards with array value type
   - If CSV type is "Choice" but has exactly 2 options:
     - Override to select_single_cards with boolean value type
   - If CSV type is inconsistent with number of options:
     - Follow the logic of the number of options
     - Document the inconsistency

### select_single_dropdown Component

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "select_single_dropdown"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always true
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required value_type and required fields
   - ✅ tooltip: Optional field (can be null)

3. **Children Structure (select_option components)**
   - ✅ Each child is a select_option component
   - ✅ Children have required fields:
     - id (UUID)
     - component_type: "select_option"
     - name: Follows naming convention (parent_name_option)
     - is_array: Always false
     - is_required: Matches parent requirement
     - is_visible: Present and boolean
     - default_value: Boolean (true/false)
     - fields: Array containing:
       - label (required)
       - description (optional)
       - image (optional)
   - ✅ Image values follow naming convention (e.g., "1_checkmark.png")
   - ✅ Default values set appropriately
   - ✅ Logic rules properly structured

4. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Component options match CSV values
   - ✅ Default selections preserved
   - ✅ Option values mapped to labels
   - ✅ Descriptions added when available
   - ✅ Images assigned based on selection type

5. **Issues Found**
   - ⚠️ Some options may lack descriptions
   - ⚠️ Image naming convention not consistent across all files
   - ⚠️ Tooltip field present but null (this is acceptable as it's optional)

6. **Recommendations**
   - Standardize image naming convention
   - Add descriptions for all options
   - Keep tooltip field as optional (null is valid)
   - Validate image file existence
   - Ensure consistent default value handling
   - Consider adding validation for option uniqueness

### select_card Component

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "select_card"
   - ✅ name: Follows naming convention (parent_name_option)
   - ✅ is_array: Always false
   - ✅ is_required: Matches parent requirement
   - ✅ is_visible: Present and boolean
   - ✅ default_value: Boolean (true/false)
   - ✅ fields: Array containing:
     - label (required)
     - description (optional)
     - image (optional)

3. **Fields Structure**
   - ✅ Each field has:
     - id (UUID)
     - name (label/description/image)
     - value (string)
   - ✅ Image values follow naming convention (e.g., "1_checkmark.png")

4. **CSV to JSON Mapping**
   - ✅ Option values mapped to card labels
   - ✅ Descriptions added when available
   - ✅ Images assigned based on selection type
   - ✅ Default values set appropriately

5. **Issues Found**
   - ⚠️ Some cards may lack descriptions
   - ⚠️ Image naming convention not consistent across all files
   - ⚠️ Tooltip field present but null (this is acceptable as it's optional)

6. **Recommendations**
   - Standardize image naming convention
   - Add descriptions for all cards
   - Keep tooltip field as optional (null is valid)
   - Validate image file existence
   - Ensure consistent default value handling

### select_option Component

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "select_option"
   - ✅ name: Follows naming convention (parent_name_option)
   - ✅ is_array: Always false
   - ✅ is_required: Matches parent requirement
   - ✅ is_visible: Present and boolean
   - ✅ default_value: Boolean (true/false)
   - ✅ fields: Array containing:
     - label (required)
     - description (optional)
     - image (optional)

3. **Fields Structure**
   - ✅ Each field has:
     - id (UUID)
     - name (label/description/image)
     - value (string)
   - ✅ Image values follow naming convention (e.g., "1_checkmark.png")

4. **CSV to JSON Mapping**
   - ✅ Option values mapped to labels
   - ✅ Descriptions added when available
   - ✅ Images assigned based on selection type
   - ✅ Default values set appropriately

5. **Issues Found**
   - ⚠️ Some options may lack descriptions
   - ⚠️ Image naming convention not consistent across all files
   - ⚠️ Tooltip field present but null (this is acceptable as it's optional)

6. **Recommendations**
   - Standardize image naming convention
   - Add descriptions for all options
   - Keep tooltip field as optional (null is valid)
   - Validate image file existence
   - Ensure consistent default value handling

### input_text_line Component (Text Box en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "input_text_line"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "string"
     - required: boolean
     - min_length (optional)
     - max_length (optional)
     - pattern (optional)
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Text Box)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ Algunos campos de texto requieren validación específica que no está implementada:
     - Códigos postales (property_zip) necesitan validación de rango
     - Campos de porcentaje (first_loan_rate) necesitan validación de formato
     - Campos de monto (purchase_price) necesitan validación de rango basada en porcentajes
   - ⚠️ Algunos campos tienen valores por defecto que no están mapeados:
     - down_payment_amount: .80 * purchase_price
     - first_loan_points: 0
     - initial_deposit_percent: 3%
   - ⚠️ Algunos campos tienen lógica condicional que no está implementada:
     - "IF not in service area, THEN pop-up message with option to sign up for notifications"
     - "IF all_cash = FALSE, THEN NEXT IS down_payment_verification"

5. **Recommendations**
   - Implementar validaciones específicas para cada tipo de campo:
     - Validación de rango para códigos postales
     - Validación de formato para porcentajes
     - Validación de rango basada en porcentajes para montos
   - Mapear correctamente los valores por defecto según el CSV
   - Implementar la lógica condicional requerida
   - Agregar mensajes de error específicos para cada tipo de validación

### input_text_area Component (Multi-line Text Box en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "input_text_area"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "string"
     - required: boolean
     - min_length (optional)
     - max_length (optional)
     - pattern (optional)
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Multi-line Text Box)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ El CSV no especifica explícitamente campos de tipo "Multi-line Text Box"
   - ⚠️ Algunos campos que podrían beneficiarse de múltiples líneas están usando "Text Box" regular:
     - contingency_property_investigation_exceptions_waived_text
     - contingency_reports_review_exceptions_other_text
     - additional_fees
     - other_report_text
   - ⚠️ No hay validaciones específicas definidas para campos multilínea
   - ⚠️ No hay límites de caracteres definidos para campos multilínea

5. **Recommendations**
   - Considerar convertir los siguientes campos a input_text_area:
     - Campos que requieren listas o múltiples entradas
     - Campos que necesitan descripciones detalladas
     - Campos que podrían beneficiarse de formato multilínea
   - Implementar validaciones específicas para campos multilínea:
     - Límites de caracteres apropiados
     - Validación de formato para listas
     - Manejo de saltos de línea
   - Agregar mensajes de error específicos para validaciones multilínea
   - Considerar agregar soporte para formato básico (listas, viñetas, etc.)

### input_email Component (Text Box en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "input_email"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "string"
     - required: boolean
     - pattern: Email format validation
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Text Box)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ El CSV especifica los campos de email como "Text Box" en lugar de un tipo específico para email
   - ⚠️ Campos de email identificados en el CSV:
     - buyer1_email
     - buyer2_email
     - buyer3_email
     - buyer4_email
     - seller1_email_fsbo
   - ⚠️ No hay validaciones específicas definidas para el formato de email
   - ⚠️ No hay restricciones de dominio definidas
   - ⚠️ No hay validación de unicidad de email

5. **Recommendations**
   - Implementar validaciones específicas para campos de email:
     - Validación de formato de email
     - Validación de dominio (opcional)
     - Validación de unicidad (opcional)
   - Agregar mensajes de error específicos para validaciones de email
   - Considerar agregar validación de dominio permitido
   - Considerar agregar validación de email único por comprador/vendedor

### input_number Component (Text Box en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "input_number"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "number"
     - required: boolean
     - min (optional)
     - max (optional)
     - step (optional)
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Text Box)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ El CSV especifica los campos numéricos como "Text Box" en lugar de un tipo específico para números
   - ⚠️ Campos numéricos identificados en el CSV:
     - property_zip (código postal)
     - property_listing_price (precio de lista)
     - purchase_price (precio de oferta)
     - first_loan_amount (monto del préstamo)
     - first_loan_rate (tasa de interés)
     - first_loan_points (puntos del préstamo)
     - additional_loan_amount (monto del préstamo adicional)
     - additional_loan_rate (tasa de interés adicional)
     - additional_loan_points (puntos del préstamo adicional)
     - initial_deposit_amount (monto del depósito inicial)
   - ⚠️ No hay validaciones específicas definidas para rangos numéricos
   - ⚠️ No hay validaciones de porcentajes para campos que lo requieren
   - ⚠️ No hay validaciones de cálculos entre campos relacionados

5. **Recommendations**
   - Implementar validaciones específicas para campos numéricos:
     - Validación de rango para códigos postales
     - Validación de rango para precios
     - Validación de rango para tasas de interés
     - Validación de rango para puntos
     - Validación de rango para depósitos
   - Implementar cálculos automáticos:
     - Porcentaje del precio de compra para préstamos
     - Porcentaje del precio de compra para depósitos
     - Cálculo de puntos basado en el monto del préstamo
   - Agregar mensajes de error específicos para cada tipo de validación
   - Considerar agregar validaciones de consistencia entre campos relacionados

### input_currency Component (Text Box en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "input_currency"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "number"
     - required: boolean
     - min (optional)
     - max (optional)
     - currency: "USD"
     - decimal_places: 2
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Text Box)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ El CSV especifica los campos de moneda como "Text Box" en lugar de un tipo específico para moneda
   - ⚠️ Campos de moneda identificados en el CSV:
     - property_listing_price (precio de lista)
     - purchase_price (precio de oferta)
     - first_loan_amount (monto del préstamo)
     - down_payment_amount (monto del pago inicial)
     - additional_loan_amount (monto del préstamo adicional)
     - initial_deposit_amount (monto del depósito inicial)
   - ⚠️ No hay validaciones específicas definidas para montos monetarios
   - ⚠️ No hay validaciones de formato de moneda
   - ⚠️ No hay validaciones de cálculos entre campos relacionados

5. **Recommendations**
   - Implementar validaciones específicas para campos de moneda:
     - Validación de formato de moneda (USD)
     - Validación de decimales (2 lugares)
     - Validación de rango para montos
     - Validación de cálculos de porcentaje
   - Implementar cálculos automáticos:
     - Porcentaje del precio de compra para préstamos
     - Porcentaje del precio de compra para depósitos
     - Cálculo de puntos basado en el monto del préstamo
   - Agregar mensajes de error específicos para cada tipo de validación
   - Considerar agregar validaciones de consistencia entre campos relacionados
   - Implementar formato de moneda consistente en toda la aplicación

### input_percentage Component (Text Box en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "input_percentage"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "number"
     - required: boolean
     - min: 0
     - max: 100
     - decimal_places: 2
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Text Box)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ El CSV especifica los campos de porcentaje como "Text Box" en lugar de un tipo específico para porcentaje
   - ⚠️ Campos de porcentaje identificados en el CSV:
     - first_loan_percent_of_price (porcentaje del préstamo sobre el precio)
     - first_loan_rate (tasa de interés)
     - first_loan_points (puntos del préstamo)
     - additional_loan_percent_of_purchase_price (porcentaje del préstamo adicional)
     - additional_loan_rate (tasa de interés adicional)
     - additional_loan_points (puntos del préstamo adicional)
     - initial_deposit_percent (porcentaje del depósito inicial)
     - increased_deposit_percent (porcentaje del depósito aumentado)
     - seller_credit_percentage (porcentaje del crédito del vendedor)
   - ⚠️ No hay validaciones específicas definidas para rangos de porcentaje
   - ⚠️ No hay validaciones de cálculos entre campos relacionados
   - ⚠️ Algunos campos tienen valores por defecto que no están mapeados

5. **Recommendations**
   - Implementar validaciones específicas para campos de porcentaje:
     - Validación de rango (0-100%)
     - Validación de decimales (2 lugares)
     - Validación de cálculos de porcentaje
   - Implementar cálculos automáticos:
     - Porcentaje del precio de compra para préstamos
     - Porcentaje del precio de compra para depósitos
     - Cálculo de puntos basado en el monto del préstamo
   - Agregar mensajes de error específicos para cada tipo de validación
   - Considerar agregar validaciones de consistencia entre campos relacionados
   - Implementar formato de porcentaje consistente en toda la aplicación

### pick_date_time Component (Date Selector en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "pick_date_time"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "string"
     - required: boolean
     - format: "YYYY-MM-DD"
     - min_date (optional)
     - max_date (optional)
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Date Selector)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ El CSV especifica los campos de fecha como "date selector" o "text box"
   - ⚠️ Campos de fecha identificados en el CSV:
     - increased_deposit_date (fecha del depósito aumentado)
     - close_of_escrow_date (fecha de cierre de escrow)
     - possession_date (fecha de posesión)
   - ⚠️ No hay validaciones específicas definidas para rangos de fechas
   - ⚠️ No hay validaciones de fechas relativas (ej: días después de la aceptación)
   - ⚠️ No hay validaciones de fechas de negocio vs. fechas calendario

5. **Recommendations**
   - Implementar validaciones específicas para campos de fecha:
     - Validación de formato de fecha
     - Validación de rango de fechas
     - Validación de fechas de negocio
     - Validación de fechas relativas
   - Implementar cálculos automáticos:
     - Fechas basadas en días después de la aceptación
     - Fechas basadas en días hábiles
     - Fechas basadas en días calendario
   - Agregar mensajes de error específicos para cada tipo de validación
   - Considerar agregar validaciones de consistencia entre campos relacionados
   - Implementar selector de fecha con calendario visual
   - Considerar agregar opción para seleccionar solo fecha o fecha y hora

### pick_file Component (Uploader en CSV)

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "pick_file"
   - ✅ name: Follows naming convention
   - ✅ is_array: Always false
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required fields:
     - value_type: "file"
     - required: boolean
     - file_types: ["pdf", "doc", "docx"]
     - max_size: "10MB"
   - ✅ tooltip: Optional field (can be null)

3. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Input type matches CSV specification (Uploader)
   - ✅ Validation rules properly mapped
   - ✅ Default values set appropriately

4. **Issues Found**
   - ⚠️ The CSV specifies file upload fields as "uploader" or "text box"
   - ⚠️ File upload fields identified in the CSV:
     - all_cash_verification_uploader (proof of funds)
     - down_payment_verification_uploader (down payment proof)
     - preapproval_letter_uploader (loan pre-approval)
   - ⚠️ No specific validations defined for file types
   - ⚠️ No file size limits defined
   - ⚠️ No validation for required document uploads
   - ⚠️ No tracking of upload status

5. **Recommendations**
   - Implement specific validations for file uploads:
     - File type validation (PDF, DOC, DOCX)
     - File size validation
     - Required document validation
     - Upload status tracking
   - Implement automatic features:
     - File type detection
     - File size calculation
     - Upload progress tracking
     - Document verification status
   - Add specific error messages for each validation type
   - Consider adding file preview capabilities
   - Implement upload status tracking in global variables
   - Add support for multiple file uploads where needed
   - Consider adding document expiration validation

## Validation Results

### select_single_cards Component

1. **Structure Validation**
   - ✅ Base structure matches documentation
   - ✅ Component type mapping is correct
   - ✅ Required properties are present

2. **Properties Validation**
   - ✅ id: Present and valid UUID
   - ✅ component_type: Correctly set as "select_single_cards"
   - ✅ name: Matches CSV specification
   - ✅ is_array: Correctly set to true
   - ✅ is_required: Matches CSV requirement
   - ✅ is_visible: Present and boolean
   - ✅ validation: Contains required value_type and required fields

3. **Children Structure (select_card components)**
   - ✅ Each child is a select_card component
   - ✅ Children have required fields:
     - id (UUID)
     - component_type: "select_card"
     - name: Follows naming convention (parent_name_option)
     - is_array: Always false
     - is_required: Matches parent requirement
     - is_visible: Present and boolean
     - default_value: Boolean (true/false)
     - fields: Array containing:
       - label (required)
       - description (optional)
       - image (optional)
   - ✅ Image values follow naming convention (e.g., "1_checkmark.png")
   - ✅ Logic rules are properly structured
   - ✅ Global variable assignments match CSV requirements

4. **CSV to JSON Mapping**
   - ✅ Screen ID matches
   - ✅ Title and description match
   - ✅ Stage and section match
   - ✅ Scope variables correctly mapped
   - ✅ Component options match CSV values
   - ✅ Option values mapped to card labels
   - ✅ Descriptions added when available
   - ✅ Images assigned based on selection type
   - ✅ Default values set appropriately

5. **Issues Found**
   - ⚠️ CSV indicates "check box" type but JSON uses select_single_cards
   - ⚠️ CSV shows "boolean" value type but JSON uses array
   - ⚠️ CSV logic format differs from JSON implementation
   - ⚠️ Some cards may lack descriptions
   - ⚠️ Image naming convention not consistent across all files
   - ⚠️ Tooltip field present but null (this is acceptable as it's optional)

6. **Recommendations**
   - Review value type consistency between CSV and JSON
   - Verify checkbox vs select_single_cards component type
   - Standardize logic rule format
   - Add validation for required fields in children
   - Ensure global variable assignments are consistent
   - Standardize image naming convention
   - Add descriptions for all cards
   - Keep tooltip field as optional (null is valid)
   - Validate image file existence
   - Ensure consistent default value handling

## Issues Found
(To be documented as we discover them)

## Next Steps
1. Begin validation with select_single_cards component
2. Document any discrepancies found
3. Update mapping documentation as needed
4. Create test cases for validated components 