from formatters import LatexFormatter
from notion_api import NotionAPI

if __name__ == "__main__":
    notion_api = NotionAPI(PAGE_ID="145bb2c6d1338027830cd4a587baf1fc")
    latex_formatter = LatexFormatter(notionapi=notion_api)
    latex_formatter.convert_blocks(notion_api.read_blocks())
