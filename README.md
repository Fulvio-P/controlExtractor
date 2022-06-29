# controlExtractor
Control extractor is tool for automatic control elicitation for the Italian Cybersecurity Framework

## Dependencies
Control extractor needs the following packages to works:
- openpyxl
- natsort

## Usage

### Basic usage:

`
python controlExtractor.py <security_templates_path> <output_xlsx_path>
`

<security_templates_path> must respect the structre of the "Security Templates" example, but it is possible to remove any unwanted function, category or subcategory by deleting the corresponding files.

<output_xlsx_path> does not have to be an existing xlsx file. If the file exists it will be overwritten, otherwise it will be created.

### Quick guide
To use controlExtractor:
1. Select from the Framework categories and subcategories for control elicitation;
2. Delete from the directories inside "Security Templates" all the files correspondind to all the unselected categories and subcategories;
3. Run the tool with the command below;

`
python controlExtractor.py Security\ Templates output.xlsx
`

### Other options
To generate controls without pre-appending an ID to each of them:

`
python controlExtractor.py <security_templates_path> <output_xlsx_path> -n
`
