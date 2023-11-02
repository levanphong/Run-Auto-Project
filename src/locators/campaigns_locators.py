# BASE PAGE
CAMPAIGN_PAGE_TAB_ITEM = "//li[contains(@class,'campaign-tab-item')]//a[contains(text(),'{}')]"
CAMPAIGN_PAGE_SEARCH_CAMPAIGN_TEXT_BOX = "//div[@class='search-inner']//input"
CAMPAIGN_PAGE_ITEM_ECLIPSE_MENU_BUTTON = "//div[contains(@class,'campaign-action')]//span"
CAMPAIGN_PAGE_EMPTY_NEW_CAMPAIGN_BUTTON = "//*[@id='empty']//*[contains(@class,'btn-create-campaign')]"
CAMPAIGN_PAGE_NEW_CAMPAIGN_BUTTON = "//*[@id='toolbar']//button[contains(text(),'New Campaign')]"
CAMPAIGN_ACTIVE_TAB = "//a[@id='tab-active']"
CAMPAIGN_PAUSED_TAB = "//a[@id='tab-paused']"
CAMPAIGN_ALL_CAMPAIGN_NAME = "//div[contains(@class,'campaign-name')]"
CAMPAIGN_ACTIONS_OPTION_DROPDOWN = "//*[contains(@class,'menu-content')]//following-sibling::*[contains(text(),'{}')]"
CAMPAIGN_TYPE_POPUP = "//*[contains(@class,'modal-content printable')]"

# BASE PAGE / Active Campaign
CAMPAIGN_ACTIVE_SETTING_ICON = "//*[contains(@class,'cursor-pt icon icon-settings')]"
CAMPAIGN_SETTING_EDIT_NAME_BUTTON = "//*[contains(text(),'Edit Name')]"

# BASE PAGE / Eclipse menu
CAMPAIGN_ITEM_ECLIPSE_MENU_DELETE_BUTTON = "//div[contains(@class,'delete')]"
CAMPAIGN_ITEM_ECLIPSE_MENU_OPTION_BUTTON = "//*[contains(text(),'{}')]"
CAMPAIGN_ITEM_ECLIPSE_MENU_PAUSE_CONFIRM_BUTTON = "//button[contains(text(),'Pause')]"

# BASE PAGE / Eclipse menu / Delete Campaign popup
CAMPAIGN_ITEM_DELETE_POPUP_DELETE_BUTTON = "(//div[@class='modal-dialog']//button[contains(@class,'btn-red')])[last()]"
CAMPAIGN_ITEM_DELETE_POPUP_CANCEL_BUTTON = "//div[contains(@class,'confirm-modal')]//button[contains(@class,'cancel-btn')]"
CAMPAIGN_ITEM_DUPLICATE_BUTTON = "//*[contains(text(),'Duplicate Campaign')]"

# BASE PAGE / Choose Campaign type popup
CHOOSE_CAMPAIGN_TYPE_POPUP_TYPE_TEXT = "//div[contains(@class,'create-campaign-modal')]//*[contains(text(),'{}')]"
CAMPAIGN_TABLE_ROW_NAME = "//*[contains(@class,'table-row clickable')]"
CAMPAIGN_TABLE_LAST_ROW_NAME = "(//*[contains(@class,'campaign-name text-overflow')])[last()]"
CAMPAIGN_ROW_NAME = "//*[contains(@class,'campaign-name text-overflow')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE
NEW_CAMPAIGN_STEP_TEXT = "//ul[@class='items']//li//span[contains(text(),'{}')]"
NEW_CAMPAIGN_NEXT_STEP_BUTTON = "//div[@class='navigation-btn']//button[contains(@class,'btn-next')]"
NEW_CAMPAIGN_BUTTON = "//button[contains(text(),'New Campaign')]"
NEW_CAMPAIGN_AI_DEFAULT_BUTTON = "//*[contains(@class,'ai-info')]//*[contains(text(),'Olivia')]"
NEW_CAMPAIGN_SEND_A_TEST_BUTTON = "//*[contains(@class,'hidden-xs')]//*[contains(text(),'Send a Test')]"
NEW_CAMPAIGN_BACK_TO_CAMPAIGN_BUTTON = "//a[@class='ev-back-btn']//*[contains(text(),'Back to Campaigns')]"
NEW_CAMPAIGN_STEP_TAB_ICON_WARN = "//*[normalize-space()='{}']//parent::*//*[@class='icon-warn']"
NEW_CAMPAIGN_LIST_HEADER = "//*[contains(@class, 'list-header')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Title and Audience step
NEW_CAMPAIGN_TITLE = "//input[@placeholder='Enter campaign title']"
NEW_CAMPAIGN_AUDIENCE_TYPE = "//div[@class='audience']//*[contains(text(),'{}')]"
NEW_CAMPAIGN_AUDIENCE_FILTER_REMOVE_ICON = "//*[contains(@class,'btn-audience-role')]//following-sibling::div//*[contains(@class,'icon-remove2')]"
NEW_CAMPAIGN_AUDIENCE_REMOVE_ICON = "//*[contains(@class,'btn-audience-role')]//*[contains(@class,'icon-remove2')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Title and Audience step / Audience dropdown
NEW_CAMPAIGN_SELECT_AUDIENCE_DROPDOWN = "//div[@class='audience']//input[@data-toggle='dropdown']"
NEW_CAMPAIGN_CANDIDATE_FROM_DROPDOWN = "//*[contains(@class,'candidate-from')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Title and Audience step / Audience filter popup
NEW_CAMPAIGN_AUDIENCE_FILTER_SEARCH_TEXT_BOX = "(//div[@class='audience']//div[contains(@class,'dropdown-menu')]//input[@placeholder='Search'])[last()]"
NEW_CAMPAIGN_AUDIENCE_FILTER_MAIN_VALUE = "//span[@class='status-icon' and contains(text(),'{}')]"
NEW_CAMPAIGN_AUDIENCE_FILTER_CHECKBOX = "//div[@class='audience']//div[@class='select-item']//div[@class='custom-checkbox']//span"
NEW_CAMPAIGN_AUDIENCE_CANDIDATE_NAME = "//*[@class='custom-checkbox']//following-sibling::*//*[contains(@class,'candidate-name')]"
NEW_CAMPAIGN_AUDIENCE_FILTER_APPLY_BUTTON = "(//div[@class='audience']//div[contains(@class,'audience-filter')]//button[contains(@class,'primary')])[last()]"
NEW_CAMPAIGN_LIST_USERS_MATCH_FIELDS_TEXT = "//*[contains(@class,'table-row header hidden-xs')]//*[contains(text(),'{}')]"
NEW_CAMPAIGN_AUDIENCE_FILTER_VALUE_OPTION = "//*[contains(@class,'dropdown-item')]//*[contains(text(),'{}')]"
NEW_CAMPAIGN_AUDIENCE_UPLOAD_BUTTON = "//*[@id='campaign-upload-button']"
NEW_CAMPAIGN_AUDIENCE_UPLOAD_FORM = "//input[@type='file']"
NEW_CAMPAIGN_AUDIENCE_UPLOAD_APPLY_BUTTON = "//*[contains(@class,'panel-footer')]//button[contains(text(),'Apply')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Title and Upload file step
CAMPAIGN_CSV_ROW_NAME = "//*[contains(@class,'csv-col-name')]"
CAMPAIGN_EXAMPLE_VALUE_ROW_NAME = "//*[contains(@class,'csv-col-name')]//following-sibling::td[1]"
CAMPAIGN_CANDIDATES_NAME_MATCHING_ROW_NAME = "//*[contains(@class,'user-name')]"
CAMPAIGN_AUDIENCE_NAME_LAST_ROW = "(//*[contains(@class,'user-name')])[last()]"
CAMPAIGN_CANDIDATE_MATCH_TEXT = "//*[contains(@class,'audience-match')]//*[contains(text(),'{}')]"
CAMPAIGN_CANDIDATES_NUMBER_TEXT = "//*[contains(@class,'audience-match')]//*[contains(@class,'title')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Title and Users step / User filter popup
NEW_CAMPAIGN_USER_FILTER_CHECKBOX = "//*[contains(@class,'section-item') and contains(text(),'{}')]//preceding-sibling::div//span"
NEW_CAMPAIGN_USER_APPLY_BUTTON = "//button[contains(text(),'Apply')]"
NEW_CAMPAIGN_USER_CANCEL_BUTTON = "//button[contains(text(),'Apply')]//preceding-sibling::button"
NEW_CAMPAIGN_USER_MATCH_LIST = "//*[contains(@class,'column name')]//*[contains(text(),'{}')]"
NEW_CAMPAIGN_USER_CLOSE_BUTTON = "//*[contains(@class,'text audience-text')]//parent::*//following-sibling::*//*[contains(@class,'icon icon-remove2')]"
NEW_CAMPAIGN_USER_LAST_CLOSE_BUTTON = "//*[contains(text(),'{}')]//parent::*//following-sibling::*//*[contains(@class,'icon icon-remove2')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Compose step
NEW_CAMPAIGN_MOBILE_CHANNEL_MESSAGE_BOX = "//div[@id='sms-preview']//div[@placeholder='- Enter your message -']"
NEW_CAMPAIGN_CAMPAIGN_TYPE_DROPDOWN = "//select[@id='campaign_type']//following-sibling::div//div"
NEW_CAMPAIGN_CAMPAIGN_TYPE_DROPDOWN_DISABLED = "//select[@id='campaign_type']//following-sibling::div//div[contains(@class,'disabled')]"
NEW_CAMPAIGN_CAMPAIGN_TYPE_DROPDOWN_VALUE = "//div[contains(@class,'campaign-type')]//div[@class='selectize-dropdown-content']//span[contains(text(),'{}')]"
NEW_CAMPAIGN_SECONDARY_OPTION = "//*[contains(@class,'v-search-box search-input white')]//following-sibling::div//span"
NEW_CAMPAIGN_CAMPAIGN_TYPE_SECOND_DROPDOWN = "//div[contains(@class, 'custom-select-drop-down__select')]"
NEW_CAMPAIGN_CAMPAIGN_TYPE_SECOND_DROPDOWN_SEARCH_TEXTBOX = "//*[contains(@class,'custom-select-drop-down__items')]//input[contains(@placeholder,'Search')]"
NEW_CAMPAIGN_COMPOSE_SELECT_CHANNEL_CHECKBOX = "//label[contains(normalize-space(),'{}')]//span"
NEW_CAMPAIGN_COMPOSE_SELECT_CHANNEL_INPUT = "//label[contains(normalize-space(),'{}')]//input"
NEW_CAMPAIGN_SMS_CHANNEL_TAB = "//*[contains(@class,'btn btn-sm btn-default btn-channel') and contains(@href,'#sms-preview')]"
NEW_CAMPAIGN_EMAIL_CHANNEL_TAB = "//*[contains(@class,'btn btn-sm btn-default btn-channel') and contains(@href,'#email-preview')]"
NEW_CAMPAIGN_SMS_CHANNEL_CHECKBOX = "//*[contains(@class,'custom-checkbox')]//*[contains(@class,'icon icon-mobile')]//following-sibling::span"
NEW_CAMPAIGN_SEND_MESSAGE_BUTTON = "//*[contains(@class,'btn btn-primary btn-sm ok-btn') and contains(text(),'Send')]"
NEW_CAMPAIGN_SECONDARY_DROPDOWN = "//*[contains(@class,'custom-select-drop-down__select form-control text-overflow') and contains(text(),'{}')]"
NEW_CAMPAIGN_SMS_CHANNEL_TITLE = "//*[contains(@class,'preview-title text-center') and contains(text(),'Create Your Introduction')]"
NEW_CAMPAIGN_COMPOSE_SENDER_FORM = "//*[contains(@class,'sender')]"
NEW_CAMPAIGN_COMPOSE_EVENT_CHECKBOX = "//*[contains(@class,'event-checkbox')]//span"
NEW_CAMPAIGN_COMPOSE_EVENT_DROPDOWN = "//*[@id='event_list']"
NEW_CAMPAIGN_COMPOSE_EVENT_DROPDOWN_SEARCH_TEXTBOX = "//input[@placeholder='Search events']"
NEW_CAMPAIGN_COMPOSE_UPLOAD_LIST_BUTTON = "//*[@id='campaign-upload-button']"
NEW_CAMPAIGN_COMPOSE_UPLOAD_LIST_ICON = "//*[@id='cpi_dropzone']//i"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Compose step / Multilingual
NEW_CAMPAIGN_MULTILINGUAL_BUTTON = "//*[contains(@data-toggle,'dropdown')]//*[contains(@class,'icon icon-multilingual')]"
NEW_CAMPAIGN_MULTILINGUAL_SEARCH_TEXTBOX = "//input[@placeholder='Search Languages']"
NEW_CAMPAIGN_MULTILINGUAL_ITEM_CHECKBOX = "//*[contains(text(),'{}')]//following-sibling::span"
NEW_CAMPAIGN_MULTILINGUAL_CONFIRM_BUTTON = "//button[contains(text(), 'Got it')]"
NEW_CAMPAIGN_MULTILINGUAL_LANGUAGE_UPDATE_CONFIRM_BUTTON = "//*[contains(@class, 'modal-footer')]//button[contains(text(), 'Confirm')]"
NEW_CAMPAIGN_MULTILINGUAL_ACTIVE_TAB = "//*[contains(@class, 'multilingual-language-tab')]//*[@class='active']"
NEW_CAMPAIGN_MULTILINGUAL_TAB = "//*[contains(@class, 'multilingual-language-tab')]//*[contains(text(), '{}')]"
NEW_CAMPAIGN_MULTILINGUAL_LANGUAGES_SELECTED = "//*[contains(@class, 'multilingual-language-tab')]//*[@class='tab-items']"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Compose step / Confirm Campaign popup
NEW_CAMPAIGN_CONFIRM_POPUP_CONFIRM_BUTTON = "(//div[@class='modal-dialog']//button[contains(@class,'btn-primary')])[last()]"
NEW_CAMPAIGN_EMAIL_CHANNEL_MESSAGE_BOX = "//div[@id='email-preview']//div[@placeholder='- Enter your message -']"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Compose step / Email
NEW_CAMPAIGN_TITLE_EMAIL_BOX = "(//*[contains(@placeholder,'Enter your email subject')])[last()]"
NEW_CAMPAIGN_EMAIL_INPUT_BOX = "//*[@id='email_send_test']"
NEW_CAMPAIGN_EMAIL_CHANNEL_CHECKBOX = "//*[contains(@class,'custom-checkbox')]//*[contains(@class,'icon icon-email')]//following-sibling::span"
NEW_CAMPAIGN_EMAIL_CONFIRM_BUTTON = "//*[contains(@class,'btn btn-primary btn-sm ok-btn') and contains(text(),'{}')]"
NEW_CAMPAIGN_EMAIL_SAVE_CONFIRM_BUTTON = "//*[contains(@class,'btn btn-primary btn-sm ok-btn') and contains(text(),'Save')]"

# BASE PAGE / New Campaign / NEW CAMPAIGN PAGE / Schedule step
NEW_CAMPAIGN_SCHEDULE_DATE_SELECTOR = "//input[@id='schedule_date']//following-sibling::input"
NEW_CAMPAIGN_SCHEDULE_DATE_SELECTOR_VALUE = "//span[contains(@class,'flatpickr-day') and not(contains(@class,'disabled')) and contains(text(),'{}')]"
NEW_CAMPAIGN_SCHEDULE_TIME_SELECTOR = "//*[@data-select2-id='1']//parent::div"
NEW_CAMPAIGN_SCHEDULE_TIME_DISABLE_SELECTOR = "//*[@data-select2-id='1']//parent::*//span[contains(@class,'disabled')]"
NEW_CAMPAIGN_SCHEDULE_TIME_SELECTOR_INPUT = "//*[@id='schedule_date']"
NEW_CAMPAIGN_SCHEDULE_MIDDAY_SELECTOR = "//*[@data-select2-id='5']//parent::div"
NEW_CAMPAIGN_SCHEDULE_MIDDLE_DISABLE_SELECTOR = "//*[@data-select2-id='5']//parent::*//span[contains(@class,'disabled')]"

# BASE PAGE / Campaign in active status
CAMPAIGN_ITEM_ECLIPSE_FIRST_USER_BUTTON = "(//*[contains(@class,'cursor-pt icon icon-menu')])[1]"
CAMPAIGN_VIEW_IN_INBOX_FIRST_BUTTON = "(//*[contains(text(),'View in Inbox')])[1]"
CAMPAIGN_LIST_AUDIENCE_TEXT = "//*[contains(@class,'custom-checkbox')]//following-sibling::*[contains(@class,'name')]"
CAMPAIGN_LIST_AUDIENCE_IN_CANDIDATE_BOX_TEXT = "//*[@data-testid='candidateblock_lbl_name']"
CAMPAIGN_THE_NUMBER_OF_CANDIDATE_TITLE = "//*[@data-testid='candidate_list_header_title']"
CAMPAIGN_NAME_TITLE = "//*[contains(@class,'pull-left header-text')]//*[contains(text(),'{}')]"
CAMPAIGN_ACTIVE_SELECT_ALL_CHECKBOX = "//*[@for='all_0']//span"
CAMPAIGN_ACTIVE_SEND_MESSAGE_BUTTON = "//*[@class='btn-resend-message']//button"
CAMPAIGN_ACTIVE_EMAIL_MESSAGE_INPUT = "//*[@id='email-preview-tab']//*[@class='emojionearea-editor']"
CAMPAIGN_ACTIVE_EMAIL_SEND_BUTTON = "//*[@class='modal-footer']//button[normalize-space()='Send']"
CAMPAIGN_ACTIVE_SETTING_EDIT_NAME = "//*[contains(@class,'sub-menu')]//*[contains(text(), 'Edit Name')]"
CAMPAIGN_ACTIVE_SEND_MESSAGE_MODAL = "//*[@id='campaign-send-message-modal']//*[@class='modal-content']"
CAMPAIGN_ACTIVE_SEND_MESSAGE_MODAL_CLOSE_BUTTON = "//*[@id='campaign-send-message-modal']//button[contains(text(),'Close')]"
CAMPAIGN_ACTIVE_STATISTICS_NUMBER = "//*[@aria-controls='{}']//*[@class='number' and contains(text(),'%')]"
CAMPAIGN_ACTIVE_STATISTICS_SENT_NUMBER = "//*[@aria-controls='Sent']//*[@class='number']"
NEW_CAMPAIGN_SCHEDULE_VALUE_HOUR = "//*[contains(@class,'select2-results')]//*[contains(text(),'{}')]"

# BASE PAGE / New Campaign / Schedule
CAMPAIGN_SCHEDULE_POPUP = "(//*[contains(@class,'modal-content printable')])[last()]"
CAMPAIGN_SCHEDULE_MESSAGE = "//*[contains(@class,'modal-body') and contains(.,'{}')]"
CAMPAIGN_CLOSE_POPUP_BUTTON = "(//button[contains(@class,'close')])[last()]"

# BASE PAGE / New Campaign / Paused
CAMPAIGN_DEFAULT_STATUS_BUTTON = "//*[contains(@class,'tab-items')]//*//following-sibling::*[contains(text(),'{}')]"
CAMPAIGN_CONFIRM_BUTTON = "//*[contains(@class,'ok-btn') and contains(text(),'Next')]"

# BASE PAGE / Drip Campaign / Campaign Step
DRIP_CAMPAIGN_ADD_CAMPAIGN_BUTTON = "//*[contains(@class,'icon-outbound-empty')]//following-sibling::*[contains(text(),'Add Campaign')]"
DRIP_CAMPAIGN_CREATE_A_NEW_CAMPAIGN_OPTION = "//*[@id='newCampaign']"
DRIP_CAMPAIGN_USE_AN_EXISTING_CAMPAIGN_TEMPLATE_OPTION = "//*[@id='newTemplateCampaign']"
DRIP_CAMPAIGN_TEMPLATE_DROPDOWN = "(//input[contains(@data-toggle,'dropdown')])[last()]"
DRIP_CAMPAIGN_SEARCH_BUTTON = "(//*[contains(@class,'vb-invisible')]//preceding-sibling::*//input)[last()]"
DRIP_CAMPAIGN_VISIBLE_SEARCH_BUTTON = "(//*[contains(@class,'vb-visible')]//preceding-sibling::*//input)[last()]"
DRIP_CAMPAIGN_CHOSEN_OPTION = "//*[contains(@class,'section-item') and text()='{}']"
DRIP_CAMPAIGN_NEW_BUTTON = "//*[contains(@class,'ai-sidebar-content')]//preceding-sibling::*//*//following-sibling::button[contains(text(),'{}')]"
DRIP_CAMPAIGN_NAME_ROW = "//*[contains(@class,'campaign-name') and contains(text(),'{}')]"
DRIP_CAMPAIGN_TITLE = "(//input[@placeholder='Enter drip campaign title'])[last()]"
DRIP_CAMPAIGN_DETAIL_TITLE = "//*[contains(@id,'campaign-drawer-modal')]//input[@placeholder='Enter drip campaign title']"
DRIP_CAMPAIGN_OPTION = "//*[contains(@class,'cusstom-radio')]//*[contains(text(),'{}')]"
DRIP_CAMPAIGN_MORE_CAMPAIGN_BUTTON = "(//*[contains(@class,'add-more-campaign')])[last()]"
DRIP_CAMPAIGN_ECLIPSE_ICON = "(//*[contains(text(),'New')]//parent::*//*[contains(@class,'icon icon-menu')])[last()]"
DRIP_CAMPAIGN_ECLIPSE_OPTION = "//*[contains(@class,'dropdown-menu')]//*[contains(text(),'{}')]"
DRIP_CAMPAIGN_DELETE_CAMPAIGN_CANCEL_BUTTON = "(//button[contains(@class,'cancel-btn')])[last()]"
DRIP_CAMPAIGN_DELETE_CAMPAIGN_DELETE_BUTTON = "(//button[contains(@class,'btn-red')])[last()]"
DRIP_CAMPAIGN_DELETE_CAMPAIGN_POPUP = "(//button[contains(@class,'btn-red')])[last()]//ancestor::*[contains(@class,'modal-content')]"
DRIP_CAMPAIGN_DUPLICATE_CAMPAIGN_MODAL = "//*[@id='campaign-drawer-modal']"
DRIP_CAMPAIGN_DUPLICATE_NAME_CAMPAIGN = "(//input[contains(@placeholder,'Enter campaign title')])[last()]"
DRIP_CAMPAIGN_AUDIENCE_IN_DUPLICATE_CAMPAIGN_TEXT = "//*[contains(@class, 'filter-text')]//span"
DRIP_CAMPAIGN_CANDIDATE_NUMBER_TEXT = "(//*[contains(@id,'campaign-info')]//*[contains(@class,'audience-match')]//*[contains(@class,'title')])[last()]"
DRIP_CAMPAIGN_DRAWER = "//*[@id='campaign-drawer-modal']"
DRIP_CAMPAIGN_ADD_CAMPAIGN_TITLE = "(//*[contains(@placeholder,'Enter drip campaign title')])[last()]"
DRIP_CAMPAIGN_ADD_CAMPAIGN_ADD_FILTER_BUTTON = "(//*[contains(text(),'{}')])[last()]"
DRIP_CAMPAIGN_ADD_CAMPAIGN_CANDIDATE_OPTION = "(//*[contains(@class,'candidate-name')])[last()]"
DRIP_CAMPAIGN_ADD_CAMPAIGN_APPLY_BUTTON = "(//*[contains(@class,'ok-btn') and contains(text(),'Apply')])[last()]"
DRIP_CAMPAIGN_ADD_CAMPAIGN_NEXT_BUTTON = "(//*[contains(@class,'btn-next')])[last()]"
DRIP_CAMPAIGN_ADD_CAMPAIGN_CANCEL_BUTTON = "(//*[contains(@class,'btn-close-drawer')])[last()]"
DRIP_CAMPAIGN_SELECT_AN_OPTION_POPUP = "//*[contains(@class,'modal-content')]//*[contains(text(),'Select an Option')]"
DRIP_CAMPAIGN_CANDIDATE_NAME_MATCHING_ROW = "(//*[contains(@class,'user-name')])[last()]"
DRIP_CAMPAIGN_CONTENT_AND_FILTER_TEXT = "(//*[contains(@class,'filter-text')])[last()]"
DRIP_CAMPAIGN_FIRST_CAMPAIGN_ADDED_TEXT = "//*[contains(@class,'first-delivery')]"
DRIP_CAMPAIGN_MESSAGE_HAVE_NOT_CAMPAIGN_TEXT = "//*[contains(@class,'drip-compose-empty')]//*[contains(text(),'You haven’t created any campaigns yet.')]"
DRIP_CAMPAIGN_SELECT_AN_OPTION_CANCEL_BUTTON = "//*[contains(text(),'Next')]//preceding-sibling::button[contains(text(),'Cancel')]"
DRIP_CAMPAIGN_ADDED_CAMPAIGN_CANDIDATE_ROW_NAME = "//*[contains(text(),'Candidates in campaign')]//ancestor::div//following-sibling::section//*[contains(@class,'user-name')]"
DRIP_CAMPAIGN_ADD_FILTER_BUTTON = "(//*[contains(text(),'Add Filter')])[last()]"
DRIP_CAMPAIGN_ADD_FILTER_IS_CAMPAIGN_OPTION = "(//*[contains(@class,'item-content')]//label[contains(text(),'is')])[1]"
DRIP_CAMPAIGN_ADD_FILTER_IS_CAMPAIGN_SEARCH_BUTTON = "(//*[contains(@class,'fa-angle-right')]//parent::*//following-sibling::*//input)[1]"
DRIP_CAMPAIGN_ADD_FILTER_IS_CAMPAIGN_SELECTED_OPTION = "(//*[contains(text(),'{}')])[1]"
DRIP_CAMPAIGN_ADD_FILTER_IS_CAMPAIGN_APPLY_BUTTON = "(//*[contains(@class,'vb-invisible')]//following-sibling::div//*[contains(text(),'Apply')])[1]"
DRIP_CAMPAIGN_ADDED_CAMPAIGN_USER_ROW_NAME = "//*[contains(text(),'Users in campaign')]//ancestor::div//following-sibling::section//*[contains(@class,'user-name')]"
DRIP_CAMPAIGN_SECOND_CHILD_CAMPAIGN_TWO_DAY_APART_TEXT = "//*[contains(text(),'{}')]//parent::*//following-sibling::*//*[contains(@class,'text-overflow')]"
DRIP_CAMPAIGN_DELIVERY_TIME_DROPDOWN_OPTION = "//*[contains(text(),'{}')]//parent::*//following-sibling::*//*//parent::*//*[contains(text(),'{}')]"
DRIP_CAMPAIGN_DELIVERY_TIME_DEFAULT_TIME_INPUT = "//*[contains(text(),'{}')]//following-sibling::*//input"
DRIP_CAMPAIGN_DELIVERY_TIME_CANCEL_BUTTON = "//*[contains(@class,'dropdown-list')]//following-sibling::*//button[contains(@class,'btn-sm')]"

# BASE PAGE / Drip Campaign / Compose step
DRIP_CAMPAIGN_MESSAGE_TEXT = "(//*[contains(@placeholder,'- Enter your message -')])[last()]"
DRIP_CAMPAIGN_AVATAR_DEFAULT_ICON = "//*[contains(@class,'ai-info')]//*[contains(@class,'avatar circle')]"
DRIP_CAMPAIGN_SMS_CHANNEL_ICON = "//*[contains(@class,'icon-mobile')]//following-sibling::span"
DRIP_CAMPAIGN_EMAIL_CHANNEL_ICON = "(//*[contains(@class,'icon-email')]//following-sibling::span)[last()]"
DRIP_CAMPAIGN_EVENT_TOGGLE_CHECKBOX = "(//*[contains(@class,'event-checkbox')]//span)[last()]"
DRIP_CAMPAIGN_ADD_CAMPAIGN_COMPOSE_BUTTON = "(//*[contains(@class,'btn-next')])[last()]"
DRIP_CAMPAIGN_ENTER_EMAIL_SUBJECT_TEXT = "(//*[contains(@placeholder,'Enter your email subject')])[last()]"
DRIP_CAMPAIGN_ENTER_EMAIL_MESSAGE_TEXT = "(//*[contains(@placeholder,'- Enter your message -')])[last()]"
DRIP_CAMPAIGN_SELECT_CAMPAIGN_TYPE_DROPDOWN = "//*[contains(@placeholder,'Select campaign type')]"
DRIP_CAMPAIGN_CHANNEL_TEXT = "(//*[contains(@class,'item-title') and contains(text(),'Message')])[1]"
DRIP_CAMPAIGN_SELECT_CAMPAIGN_TYPE_DROPDOWN_OPTION = "//*[contains(@class,'selectize-dropdown-content')]//span[contains(text(),'Message')]"
DRIP_CAMPAIGN_SELECT_AN_EVENT_DROPDOWN = "//*[contains(@value,'Select an Event')]"
DRIP_CAMPAIGN_SEARCH_EVENT_BUTTON = "//*[contains(@placeholder,'Search events')]"
DRIP_CAMPAIGN_EVENT_DROPDOWN_OPTION = "(//*[contains(@class,'event-name')])[last()]"
DRIP_CAMPAIGN_SEARCH_FILTER_INPUT = "(//*[contains(@class,'btn-audience-role')]//following-sibling::*//*[contains(@placeholder, 'Search')])[last()]"
DRIP_CAMPAIGN_FILTER_OPTION = "(//*[contains(@class,'status-icon') and contains(text(),'{}')])[last()]"
DRIP_CAMPAIGN_AUDIENCE_SEARCH_INPUT = "(//*[contains(@class,'audience-filter')]//following-sibling::*//*[contains(@placeholder, 'Search')])[last()]"
DRIP_CAMPAIGN_FIRST_CANDIDATE_OPTION = "(//*[contains(@class,'candidate-name') and contains(text(),'{}')])[1]"

# BASE PAGE / Drip Campaign / Active status
DRIP_CAMPAIGN_VALUE_CAMPAIGN_TEXT = "//*[contains(@class,'campaign-select')]"
DRIP_CAMPAIGN_VALUE_CAMPAIGN_LIST = "//*[contains(@class,'section-item')]"
DRIP_CAMPAIGN_VALUE_CAMPAIGN_ROW = "//*[contains(@class,'section-item') and contains(text(),'{}')]"
DRIP_CAMPAIGN_CANDIDATE_NAME_ROW = "//*[contains(@class,'column audience-name')]//*//following-sibling::div//span"
DRIP_CAMPAIGN_SETTING_ICON = "//*[contains(@class,'menu-content')]//*[contains(text(),'Edit')]"

# BASE PAGE / Drip Campaign / Schedule step
DRIP_CAMPAIGN_END_DRIP_CAMPAIGN_TOGGLE = "//*[contains(@class,'toggle-btn large')]"
DRIP_CAMPAIGN_SCHEDULE_DAY_SELECTOR = "(//div[contains(@class,'form-group has-feedback')]//input//following-sibling::input)[last()]"
DRIP_CAMPAIGN_SCHEDULE_DAY_SELECTOR_VALUE = "(//*[contains(@class,'flatpickr-day') and not(contains(@class,'disabled')) and contains(text(),'{}')])[last()]"
DRIP_CAMPAIGN_SCHEDULE_CONFIRM_MESSAGE = "//*[contains(@class,'modal-body') and contains(text(),'{}')]"
DRIP_CAMPAIGN_SCHEDULE_CONTAIN_AUDIENCES_MESSAGE = "//*[contains(@class,'modal-body')]//b"