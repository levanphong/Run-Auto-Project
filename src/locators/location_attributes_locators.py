LEFT_MENU_OPTION_BY_NAME = "//*[contains(@class,'nav-item_text')]//*[text()='{}']"
ATTRIBUTE_NAME = "//*[contains(@class,'data-list-container')]//*[contains(@class,'column-name')]//*[text()='{}']"
TEXTBOX_SEARCH_ATTRIBUTES = "//input[contains(@placeholder,'Search attributes')]"
LIST_LOCATION_ATTRIBUTES = "//*[contains(@class,'data-list-container')]//*[contains(@class,'column-name')]"
TEXT_NO_RESULT_FOUND = "//*[contains(@class,'data-list empty')]//*[contains(text(),'No results found')]"
INPUT_ATTRIBUTE_DESCRIPTION = "id:id_attribute_desc"
TOGGLE_ATTRIBUTE_REPORT = "//*[contains(@for,'id_add_to_report')]"
BUTTON_SAVE = "//button[contains(@class,'btn-primary') and contains(text(),'Save')]"
BUTTON_CANCEL = "//*[contains(@class,'pull-right')]//button[contains(@class,'btn-default') and contains(text(),'Cancel')]"
INPUT_ATTRIBUTE_NAME = "id:id_attribute_name"
INPUT_ATTRIBUTE_KEY = "id:id_attribute_key"
ATTRIBUTE_DESCRIPTION = "//*[contains(@class,'data-list-container')]//*[contains(@class,'column-desc')]//*[contains(text(),'{}')]"
ATTRIBUTE_REQUIRED_FIELD_ERROR = "//label[contains(text(), '{}')]//ancestor::div[contains(@class, 'has-error')]//span[contains(text(), 'Field required.')]"
LOCATION_ATTRIBUTE_TOOLTIP_MESSAGE = "//*[contains(@class,'popup_container--on-hover')]//*[contains(text(),'{}')]"
EMPTY_LOCATION_ATTRIBUTE_MESSAGE = "//*[contains(@class,'empty-location-attr')]//*[contains(text(),'You haven’t created any location attributes yet.')]"
TITLE_LOCATION_ATTRIBUTE = "//*[contains(@class,'title')]//*[contains(text(),'{}')]"
HEADER_ATTRIBUTE_NAME = "//*[contains(@class,'header')]//*[contains(text(),'Attribute Name')]"
HEADER_KEY_NAME = "//*[contains(@class,'header')]//*[contains(text(),'Key Name')]"
HEADER_DESCRIPTION = "//*[contains(@class,'header')]//*[contains(text(),'Description')]"
HEADER_LAST_EDITED = "//*[contains(@class,'header')]//*[contains(text(),'Last Edited')]"
BUTTON_ADD_ATTRIBUTE = "//button[contains(@class,'btn-primary')]//*[contains(text(),'Add Attribute')]"
BUTTON_CREATE = "//button[contains(@class,'btn-primary') and contains(text(),'Create')]"
BUTTON_ELLIPSE = "//*[contains(@class,'column-name')]//*[text()='{}']/ancestor::*[contains(@class,'items')]//*[@id='sub-menu']"
BUTTON_EDIT_SUBMENU = "//*[contains(@class,'column-name')]//*[text()='{}']/ancestor::*[contains(@class,'items')]//*[contains(@data-action-id,'edit')]"
BUTTON_DELETE_SUBMENU = "//*[contains(@class,'column-name')]//*[text()='{}']/ancestor::*[contains(@class,'items')]//*[contains(@data-action-id,'delete')]"
TEXT_INFOR_SUBMENU = "//*[contains(@class,'column-name')]//*[text()='{}']/ancestor::*[contains(@class,'items')]//*[contains(@class,'info') and contains(text(),'Created on')]"
TITLE_MODAL = "//*[contains(@class,'modal-title') and contains(text(),'{}')]"
CONTENT_MODAL = "//*[contains(@class,'modal-body') and contains(text(),'{}')]"
BUTTON_CANCEL_MODAL_DELETE = "(//button[contains(@class,'cancel-btn') and contains(text(),'Cancel')])[last()]"
BUTTON_OK_MODAL_DELETE = "//button[contains(@class,'ok-btn') and contains(text(),'Delete')]"
SUCCESS_ALERT = "//*[contains(@role,'alert')]//*[contains(text(),'{}')]"
BUTTON_NEW_ATTRIBUTE = "//button[contains(@class,'btn-primary')]//*[contains(text(),'New Attribute')]"
OUTSIDE_FRAME = "//*[contains(@class,'column-layout__right')]"
