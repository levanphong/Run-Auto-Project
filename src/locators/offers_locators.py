# BASE PAGE
SEARCH_OFFER_TEXT_BOX = "//input[@placeholder='Search offer']"
OFFER_LIST_ECLIPSE_ICON = "//i[@class='icon icon-menu']"
OFFER_NAME = "//div[contains(text(),'{}')]"
MENU_ICON_BY_OFFERS_NAME_TO_DELETE = "//div[contains(text(), '{}')]//ancestor::tr//span[contains(text(), '0 Job')]//ancestor::tr//i[contains(@class, 'icon-menu')]"
OFFER_LIST_ITEM_MENU = "//div[contains(text(), '{}')]//ancestor::td//following-sibling::td//button[contains(@aria-controls, 'dropdown-menu')]"

# BASE PAGE / Eclipse popup
OFFER_ECLIPSE_POPUP_ICON_EDIT_ICON = "(//i[contains(@class, 'icon-edit')])[last()]"
OFFER_ECLIPSE_POPUP_ICON_PREVIEW_ICON = "(//i[contains(@class, 'icon-preview')])[last()]"
OFFER_ECLIPSE_POPUP_ICON_DELETE_ICON = "(//i[contains(@class, 'icon-delete')])[last()]"
OFFER_ECLIPSE_POPUP_ICON_DUPLICATE_ICON = "(//i[contains(@class, 'icon-duplicate')])[last()]"

# Offer create page
OFFER_CONTENT_EDITOR = "//div[contains(@class,'ql-editor')]"
OFFER_QUILL_MENTION_LIST = "//li[contains(@id,'quill-mention-item')]"
OFFER_QUILL_MENTION_VALUE = "//li[contains(@id,'quill-mention-item') and text()='{}']"
OFFER_QUILL_MENTION_HIGHLIGHT_VALUE = "//span[@class='highlight-token' and @data-value='{}']"
NEW_OFFER_NAME_TEXT_BOX = "//span[contains(@class,'color-lighter naming_mask__input__placeholder')]"
NEW_OFFER_CREATE_BUTTON = "//button[@data-testid='offer_builder_btn_save_page']"
NEW_OFFER_PUBLISH_STATUS = "//span[@data-testid='offer_status_bar_lbl_status']"
NEW_OFFER_PUBLISH_BUTTON = "//button[@data-testid='offer_status_bar_btn_publish']"
NEW_OFFER_ATTRIBUTE = "//span[contains(@class, 'highlight-token') and contains(@data-value, '{}')]"
NEW_OFFER_COMPONENT_LABEL = "//span[contains(@data-label, '{}')]"
NEW_OFFER_TEMPLATE_EDITOR = "(//div[contains(@class, 'ql-editor')]//p[contains(text(), 'Sincerely')])[last()]"
NEW_OFFER_COMPONENT_BUILDER_OPTION = "//span[@data-testid='offer_toolbar_lbl_add_type' and contains(text(), '{}')]"
NEW_OFFER_ADD_COMPONENT_BUILDER = "//span[@data-testid='offer_toolbar_lbl_add_type' and contains(text(), '{}')]//parent::div//following-sibling::button[contains(@data-testid, 'offer_toolbar_btn_add_type')]"
NEW_OFFER_REMOVE_COMPONENT_ICON = "//span[contains(@class, 'offer-token-delete')]"
NEW_OFFER_DELETE_COMPONENT_ICON= "//span[contains(@data-label,'{}')]//i[contains(@class,'icon-delete')]"
NEW_OFFER_REMOVE_COMPONENT_CONFIRM = "//div[contains(@aria-label, 'Delete')]//button//span[contains(text(), 'Delete')]"
NEW_OFFER_CANCEL_REMOVE_COMPONENT = "//div[contains(@aria-label, 'Delete')]//button//span[contains(text(), 'Cancel')]"
NEW_OFFER_CLOSE_REMOVE_COMPONENT = "//div[contains(@aria-label, 'Delete')]//button//i[contains(@class, 'icon-close')]"

# Offer create page - Add Component builder
NEW_OFFER_COMPONENT_NAME_INPUT = "//input[@data-testid='offer_label_toolbar_input_title']"
NEW_OFFER_COMPONENT_VALIDATION_DROPDOWN = "//div[@data-testid='offer_validation_select_id']"
NEW_OFFER_COMPONENT_SEARCH_LOCATION_VALIDATION = "//span[@data-testid='offer_validation_lbl_search_location']"
NEW_OFFER_COMPONENT_SEARCH_NAME_VALIDATION = "//span[@data-testid='offer_validation_lbl_search_name']"
NEW_OFFER_COMPONENT_VALIDATION_OPTION = "//li[contains(@class, 'el-select-dropdown') and normalize-space()='{}']"
NEW_OFFER_COMPONENT_SYSTEM_ATTRIBUTE_DROPDOWN = "//div[contains(@data-testid, 'offer_attribute_input')]//input"
NEW_OFFER_COMPONENT_STORE_ATTRIBUTE_DROPDOWN = "(//div[contains(@data-testid, 'offer_attribute_input')])[2]//input"
NEW_OFFER_COMPONENT_SYSTEM_ATTRIBUTE_VALUE = "//li[contains(@data-testid, 'offer_attribute_option') and normalize-space()='{}']"
NEW_OFFER_COMPONENT_STORE_ATTRIBUTE_VALUE = "//li[contains(@data-testid, 'offer_store_attribute_option') and normalize-space()='{}']"
NEW_OFFER_COMPONENT_DESTINATION_FIELD = "//input[contains(@data-testid, 'offer_ats_destination_input')]"
NEW_OFFER_COMPONENT_ADD_BUTTON = "(//div[contains(@class, 'footer')]//span[text()='Add'])[last()]"
NEW_OFFER_COMPONENT_CANCEL_BUTTON = "(//div[contains(@class, 'footer')]//span[text()='Cancel'])[last()]"
NEW_OFFER_COMPONENT_DELETE_BUTTON = "(//div[contains(@class, 'footer')]//span[text()='Delete'])[last()]"
NEW_OFFER_COMPONENT_SAVE_BUTTON = "(//div[contains(@class, 'footer')]//span[text()='Save'])[last()]"
NEW_OFFER_COMPONENT_CLOSE_ICON = "(//button[contains(@class, 'close-btn')]//i[contains(@class, 'icon-close')])[last()]"
NEW_OFFER_INPUT_DOCUMENT = "//input[@type='file']"
NEW_OFFER_DOCUMENT_LABEL= "//i[contains(@class, 'icon icon-offer')]//following-sibling::div"
NEW_OFFER_DROPDOWN_OPTION_WITH_INDEX = "(//input[contains(@placeholder, 'Enter Option')])[{}]"
NEW_OFFER_COMPONENT_CURRENCY_DROPDOWN = "//div[@data-testid='offer_currency_select_id']"
NEW_OFFER_COMPONENT_CURRENCY_OPTION = "//li[contains(@data-testid, 'offer_currency')]//span[contains(text(), '{}')]"
NEW_OFFER_COMPONENT_CURRENCY_SEARCH = "//input[contains(@placeholder, 'Search currency')]"
NEW_OFFER_COMPONENT_PAY_FREQUENCY_DROPDOWN = "//input[contains(@placeholder, 'Select frequency')]"
NEW_OFFER_COMPONENT_PAY_FREQUENCY_OPTION = "//input[contains(@type, 'checkbox')]//parent::span//following-sibling::span//span[contains(text(), '{}')]"
NEW_OFFER_COMPONENT_PAY_FREQUENCY_STATUS = "//span[contains(text(), '{}')]//parent::span//parent::label"
NEW_OFFER_COMPONENT_LANGUAGE_ICON = "//i[contains(@class, 'icon-multilingual')]"
NEW_OFFER_COMPONENT_LANGUAGE_OPTION = "//span[contains(@class, 'el-checkbox') and contains(text(), '{}')]"
NEW_OFFER_COMPONENT_LANGUAGE_TAB = "//div[contains(@class, 'el-tabs') and contains(text(), '{}')]"
NEW_OFFER_REMOVE_FIELD_MAPPING = "//i[@class='icon icon-delete2']"

# Offer create page / Publish Offer popup
PUBLISH_OFFER_POPUP_PUBLISH_BUTTON = "//div[contains(@class, 'ol-confirm')]//button//span[contains(text(),'Publish')]"
PUBLISH_OFFER_POPUP_CANCEL_BUTTON = "//div[contains(@class, 'ol-confirm')]//button//span[contains(text(), 'Cancel')]"
PUBLISH_OFFER_SUCCESS_TOASTED = "//*[contains(@class, 'toasted toasted-primary success')]"
PUBLISH_OFFER_ERROR_TOASTED = "//*[contains(@class, 'toasted toasted-primary error')]"

# Offer create page / Delete Component popup
DELETE_COMPONENT_POPUP_CANCEL_DELETE_BUTTON= "//*[contains(@class,'el-message-box ol-confirm')]//*[contains(@type,'button')]//*[contains(text(),'{}')]"

# OFFER LETTER PAGE
OPEN_OFFER_VERIFY_CODE_1  = "(//input[contains(@inputmode, 'numeric')])[1]"
OPEN_OFFER_VERIFY_CODE_2  = "(//input[contains(@inputmode, 'numeric')])[2]"
OPEN_OFFER_VERIFY_CODE_3  = "(//input[contains(@inputmode, 'numeric')])[3]"
OPEN_OFFER_VERIFY_CODE_4  = "(//input[contains(@inputmode, 'numeric')])[4]"
OPEN_OFFER_VERIFY_CODE_5  = "(//input[contains(@inputmode, 'numeric')])[5]"
OPEN_OFFER_VERIFY_CODE_6  = "(//input[contains(@inputmode, 'numeric')])[6]"
ACTION_IN_OFFER_ACCEPT_BUTTON = "//*[contains(@class,'candidate-actions')]//*[normalize-space(text())='Accept']"
ACTION_IN_OFFER_DO_NOT_ACCEPT_BUTTON = "//*[contains(@class,'candidate-actions')]//*[normalize-space(text())='Do Not Accept']"
OFFER_DOWNLOAD_ICON = "//i[contains(@class, 'icon-download')]"
OFFER_DOWNLOAD_SUCCESS_TOASTED = "//*[contains(@class, 'toasted toasted-primary default')]"
OFFER_VIEW_ICON = "//span[contains(text(), '{}')]//ancestor::div[contains(@class, 'offer-document-item-inner')]//span[contains(text(), 'View')]"
OFFER_CHECK_ICON= "//span[contains(text(), '{}')]//ancestor::div[contains(@class, 'offer-document-item-inner')]//i[contains(@class, 'icon-check')]"

# OFFER PREVIEW PAGE
OFFER_PREVIEW_SEARCH_LOCATION_DROPDOWN = "//div[contains(@data-testid, 'location_form_search_location')]//input"
OFFER_PREVIEW_SEARCH_USER_NAME_DROPDOWN = "//div[contains(@data-testid, 'user_form_search_user')]//input"
OFFER_ICON_CLOSE = "//div[contains(@data-testid, 'form_search')]//i[contains(@class, 'icon-remove')]"
OFFER_PREVIEW_SEARCH_LOCATION_DROPDOWN_VALUE = "//li[contains(@class, 'el-select-dropdown') and normalize-space()='{}']"
OFFER_PREVIEW_SEARCH_USER_DROPDOWN_VALUE = "//li[contains(@class, 'el-select-dropdown')]//div[normalize-space()='{}']"
