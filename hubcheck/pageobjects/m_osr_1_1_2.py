# represents hubs updated between December 2012 - February 2013
from marrow import *

# load page objects
from po_admin_login_page import AdminLoginPage
from po_courses_page import CoursesPage
from po_filexfer_exportfile_page import FilexferExportfilePage
from po_filexfer_importfile_page import FilexferImportfilePage
from po_generic_page import GenericPage
from po_groups_base import GroupsBasePage
from po_groups_delete_page import GroupsDeletePage
from po_groups_invite_page import GroupsInvitePage
from po_groups_new_page import GroupsNewPage
from po_groups_overview_page import GroupsOverviewPage
from po_groups_page import GroupsPage
from po_groups_wiki_article_page import GroupsWikiArticlePage
from po_groups_wiki_base_page import GroupsWikiBasePage
from po_groups_wiki_delete_page import GroupsWikiDeletePage2 as GroupsWikiDeletePage
from po_groups_wiki_edit_page import GroupsWikiEditPage2 as GroupsWikiEditPage
from po_groups_wiki_new_page import GroupsWikiNewPage2 as GroupsWikiNewPage
from po_groups_wiki_rename_page import GroupsWikiRenamePage2 as GroupsWikiRenamePage
from po_hubucoursebase import HubUCourseBasePage
from po_hubucoursehome import HubUCourseHomePage
from po_hubucoursemanage import HubUCourseManagePage
from po_hubucoursemanagedashboard import HubUCourseManageDashboardPage
from po_hubucoursemanageemail import HubUCourseManageEmailPage
from po_hubucoursemanageinvites import HubUCourseManageInvitesPage
from po_hubucoursemanagemembership import HubUCourseManageMembershipPage
from po_login import LoginPage1 as LoginPage
from po_loginremind import LoginRemindPage
from po_loginreset import LoginResetPage
from po_members_change_password import MembersChangePasswordPage
from po_members_dashboard import MembersDashboardPage
from po_members_profile import MembersProfilePage
from po_register import RegisterPage
from po_resources_tool_attachments_page import ResourcesToolAttachmentsPage
from po_resources_tool_contributors_page import ResourcesToolContributorsPage
from po_resources_tool_description_page import ResourcesToolDescriptionPage
from po_resources_tool_finalize_page import ResourcesToolFinalizePage
from po_resources_tool_tags_page import ResourcesToolTagsPage
from po_resourcespage import ResourcesPage
from po_resourcesnewattachpage import ResourcesNewAttachPage
from po_resourcesnewauthorspage import ResourcesNewAuthorsPage
from po_resourcesnewcomposepage import ResourcesNewComposePage
from po_resourcesnewpage import ResourcesNewPage
from po_resourcesnewreviewpage import ResourcesNewReviewPage
from po_resourcesnewtagspage import ResourcesNewTagsPage
from po_support_page import SupportPage
from po_supportneedhelp import SupportNeedHelpPage
from po_supportticketview import SupportTicketViewPage
from po_supportticketnew import SupportTicketNewPage
from po_supportticketsave import SupportTicketSavePage
from po_supportticketsearch import SupportTicketSearchPage2012 as SupportTicketSearchPage
from po_tags_browse_page import TagsBrowsePage
from po_tags_page import TagsPage
from po_tags_view_page import TagsViewPage
from po_time_base_page import TimeBasePage
from po_time_new_hub_page import TimeNewHubPage
from po_time_new_record_page import TimeNewRecordPage
from po_time_new_task_page import TimeNewTaskPage
from po_time_overview_page import TimeOverviewPage
from po_tool_session_page import ToolSessionPage2 as ToolSessionPage
from po_tools_create_page import ToolsCreatePage
from po_tools_pipeline_page import ToolsPipelinePage
from po_tools_status_approve_confirm_license_page import ToolsStatusApproveConfirmLicensePage
from po_tools_status_approve_confirm_toolinfo_page import ToolsStatusApproveConfirmToolInfoPage
from po_tools_status_approve_confirm_version_page import ToolsStatusApproveConfirmVersionPage
from po_tools_status_approved_page import ToolsStatusApprovedPage, ToolsStatusApprovedAdminPage
from po_tools_status_base_page import ToolsStatusBasePage, ToolsStatusBaseAdminPage
from po_tools_status_created_page import ToolsStatusCreatedPage, ToolsStatusCreatedAdminPage
from po_tools_status_installed_page import ToolsStatusInstalledPage, ToolsStatusInstalledAdminPage
from po_tools_status_published_page import ToolsStatusPublishedPage, ToolsStatusPublishedAdminPage
from po_tools_status_registered_page import ToolsStatusRegisteredPage, ToolsStatusRegisteredAdminPage
from po_tools_status_uploaded_page import ToolsStatusUploadedPage, ToolsStatusUploadedAdminPage
from po_wishlistsearch import WishlistSearchPage
from po_wishlistnewwish import WishlistNewWishPage


# load widgets
from widgets.admin_login import AdminLogin1 as AdminLogin
from widgets.captcha1 import Captcha1
from widgets.captcha2 import Captcha2
from widgets.courses import Courses
from widgets.dashboard_membership import DashboardMembership
from widgets.dashboard_tickets import DashboardTickets
from widgets.footer import Footer
from widgets.groups import Groups1 as Groups
from widgets.groups_customize_form import GroupsCustomizeForm1 as GroupsCustomizeForm
from widgets.groups_delete_form import GroupsDeleteForm
from widgets.groups_info import GroupsInfo1 as GroupsInfo
from widgets.groups_invite_form import GroupsInviteForm
from widgets.groups_member_browser import GroupsMemberBrowser
from widgets.groups_menu import GroupsMenu1 as GroupsMenu
from widgets.groups_new_form import GroupsNewForm1 as GroupsNewForm
from widgets.groups_options import GroupsOptions
from widgets.groups_overview import GroupsOverview1 as GroupsOverview
from widgets.groups_title import GroupsTitle2 as GroupsTitle
from widgets.groups_wiki import GroupsWiki
from widgets.groups_wiki_article import GroupsWikiArticle
from widgets.groups_wiki_delete_form import GroupsWikiDeleteForm
from widgets.groups_wiki_edit_form import GroupsWikiEditForm1 as GroupsWikiEditForm
from widgets.groups_wiki_menu import GroupsWikiMenu1 as GroupsWikiMenu
from widgets.groups_wiki_new_form import GroupsWikiNewForm1 as GroupsWikiNewForm
from widgets.groups_wiki_rename_form import GroupsWikiRenameForm
from widgets.header import Header1 as Header
from widgets.hubu_course_login import HubUCourseLogin
from widgets.hubu_course_manage_emailform import HubUCourseManageEmailForm
from widgets.hubu_course_manage_tabs import HubUCourseManageTabs
from widgets.hubu_course_membership_listing import HubUCourseMembershipListing
from widgets.hubu_course_membership_listing_detail_row import HubUCourseMembershipListingDetailRow
from widgets.hubu_course_membership_listing_member_row import HubUCourseMembershipListingMemberRow
from widgets.hubu_course_menu import HubUCourseMenu
from widgets.iframewrap import IframeWrap
from widgets.item_list import ItemList
from widgets.listpagenav import ListPageNav2 as ListPageNav
from widgets.listtopcounts import ListTopCounts
from widgets.login_base import Login
from widgets.login_remind_form import LoginRemindForm
from widgets.login_reset_form import LoginResetForm
from widgets.members_change_password_form import MembersChangePasswordForm
from widgets.members_dashboard_my_sessions import MembersDashboardMySessions
from widgets.members_dashboard_my_sessions_item import MembersDashboardMySessionsItem
from widgets.members_dashboard_my_sessions_storage import MembersDashboardMySessionsStorage
from widgets.members_dashboard_table import MembersDashboardTable1 as MembersDashboardTable
from widgets.members_pagemenu import MembersPageMenu
from widgets.members_profile_biography import MembersProfileBiography
from widgets.members_profile_citizenship import MembersProfileCitizenship
from widgets.members_profile_element import MembersProfileElement
from widgets.members_profile_email import MembersProfileEmail
from widgets.members_profile_employment import MembersProfileEmployment
from widgets.members_profile_form import MembersProfileForm3 as MembersProfileForm
from widgets.members_profile_gender import MembersProfileGender
from widgets.members_profile_interests import MembersProfileInterests
from widgets.members_profile_mailpreference import MembersProfileMailPreference1 as MembersProfileMailPreference
from widgets.members_profile_name import MembersProfileName
from widgets.members_profile_organization import MembersProfileOrganization
from widgets.members_profile_password import MembersProfilePassword
from widgets.members_profile_residence import MembersProfileResidence
from widgets.members_profile_website import MembersProfileWebsite
from widgets.members_profile_telephone import MembersProfileTelephone
from widgets.need_help_form import NeedHelpForm
from widgets.popular_item import PopularItem
from widgets.popular_list import PopularList
from widgets.register_form import RegisterForm2 as RegisterForm
from widgets.resources import Resources
from widgets.resources_category_browser import ResourcesCategoryBrowser
from widgets.resources_new import ResourcesNew
from widgets.resources_new_attach_form import ResourcesNewAttachForm
from widgets.resources_new_authors_authors_list import ResourcesNewAuthorsAuthorsList
from widgets.resources_new_authors_authors_form import ResourcesNewAuthorsAuthorsForm
from widgets.resources_new_authors_form import ResourcesNewAuthorsForm
from widgets.resources_new_compose_form import ResourcesNewComposeForm1 as ResourcesNewComposeForm
from widgets.resources_new_review_form import ResourcesNewReviewForm
from widgets.resources_new_tags_form import ResourcesNewTagsForm
from widgets.resources_tool_attachments_form import ResourcesToolAttachmentsForm
from widgets.resources_tool_contributors_form import ResourcesToolContributorsForm
from widgets.resources_tool_description_form import ResourcesToolDescriptionForm1 as ResourcesToolDescriptionForm
from widgets.resources_tool_file_upload_row import ResourcesToolFileUploadRow
from widgets.resources_tool_finalize_form import ResourcesToolFinalizeForm
from widgets.resources_tool_screenshot_upload_row import ResourcesToolScreenshotUploadRow
from widgets.resources_tool_tags_form import ResourcesToolTagsForm
from widgets.search_results import SearchResults
from widgets.sort_order_options import SortOrderOptions
from widgets.storage_meter import StorageMeter
from widgets.support import Support2 as Support
from widgets.tag_search_box import TagSearchBox
from widgets.tags import Tags
from widgets.tags_browse_form import TagsBrowseForm
from widgets.tags_browse_order_options import TagsBrowseOrderOptions
from widgets.tags_browse_results_row import TagsBrowseResultsRow1 as TagsBrowseResultsRow
from widgets.tags_view_form import TagsViewForm
from widgets.tags_view_results_row import TagsViewResultsRow
from widgets.tags_list import TagsList
from widgets.text_search_box import TextSearchBox
from widgets.ticket_comment import TicketComment
from widgets.ticket_comment_form import TicketCommentForm
from widgets.ticket_comment_list import TicketCommentList
from widgets.ticket_comment_base import TicketCommentBase
from widgets.ticket_content import TicketContent
from widgets.ticket_list_filter_options import TicketListFilterOptions
from widgets.ticket_list_search_form import TicketListSearchForm
from widgets.ticket_list_search_result_row import TicketListSearchResultRow
from widgets.ticket_list_sort_options import TicketListSortOptions
from widgets.ticket_new_form import TicketNewForm
from widgets.ticket_save import TicketSave
from widgets.time_navigation import TimeNavigation
from widgets.time_new_hub_form import TimeNewHubForm
from widgets.time_new_record_form import TimeNewRecordForm
from widgets.time_new_task_form import TimeNewTaskForm
from widgets.time_overview import TimeOverview
from widgets.tool_session_app import ToolSessionApp
from widgets.tool_session_app_storage import ToolSessionAppStorage
from widgets.tool_session_share import ToolSessionShare
from widgets.tool_session_shared_with_item import ToolSessionSharedWithItem
from widgets.tools_create_form import ToolsCreateForm
from widgets.tools_pipeline_filter_options import ToolsPipelineFilterOptions
from widgets.tools_pipeline_search_form import ToolsPipelineSearchForm
from widgets.tools_pipeline_search_result_row import ToolsPipelineSearchResultRow
from widgets.tools_pipeline_sort_options import ToolsPipelineSortOptions
from widgets.tools_status_administrator_controls import ToolsStatusAdministratorControls
from widgets.tools_status_administrator_form import ToolsStatusAdministratorForm
from widgets.tools_status_approve_license_form import ToolsStatusApproveLicenseForm
from widgets.tools_status_approve_toolinfo_form import ToolsStatusApproveToolInfoForm
from widgets.tools_status_approve_version_form import ToolsStatusApproveVersionForm
from widgets.tools_status_approved import ToolsStatusApproved
from widgets.tools_status_base import ToolsStatusBase
from widgets.tools_status_created import ToolsStatusCreated
from widgets.tools_status_developer_tools import ToolsStatusDeveloperTools
from widgets.tools_status_installed import ToolsStatusInstalled
from widgets.tools_status_published import ToolsStatusPublished
from widgets.tools_status_registered import ToolsStatusRegistered
from widgets.tools_status_remaining_steps import ToolsStatusRemainingSteps
from widgets.tools_status_tool_info import ToolsStatusToolInfo
from widgets.tools_status_uploaded import ToolsStatusUploaded
from widgets.tools_status_whats_next_approved import ToolsStatusWhatsNextApproved
from widgets.tools_status_whats_next_created import ToolsStatusWhatsNextCreated
from widgets.tools_status_whats_next_installed import ToolsStatusWhatsNextInstalled
from widgets.tools_status_whats_next_published import ToolsStatusWhatsNextPublished
from widgets.tools_status_whats_next_registered import ToolsStatusWhatsNextRegistered
from widgets.tools_status_whats_next_uploaded import ToolsStatusWhatsNextUploaded
from widgets.tools_status_version_list_row import ToolsStatusVersionListRow
from widgets.trouble_report_form import TroubleReportForm
from widgets.upload2 import Upload2 as Upload2
from widgets.upload_list1 import UploadList1
from widgets.upload_list2 import UploadList2
from widgets.wiki_text_area import WikiTextArea
from widgets.wishlist_search_form import WishlistSearchForm
from widgets.wishlist_filter_options import WishlistFilterOptions
from widgets.wishlist_new_wish_form import WishlistNewWishForm
from widgets.wishlist_order_options import WishlistOrderOptions
from widgets.wishlist_search_result_row import WishlistSearchResultRow
from widgets.wishlist_search_result_row_detail import WishlistSearchResultRowDetail
from widgets.wishlist_vote import WishlistVote

# load page object locators
from po_admin_login_page import AdminLoginPage_Locators_Base as AdminLoginPage_Locators
from po_courses_page import CoursesPage_Locators_Base as CoursesPage_Locators
from po_filexfer_exportfile_page import FilexferExportfilePage_Locators_Base as FilexferExportfilePage_Locators
from po_filexfer_importfile_page import FilexferImportfilePage_Locators_Base as FilexferImportfilePage_Locators
from po_generic_page import GenericPage_Locators_Base_1 as GenericPage_Locators
from po_groups_base import GroupsBasePage_Locators_Base as GroupsBasePage_Locators
from po_groups_delete_page import GroupsDeletePage_Locators_Base as GroupsDeletePage_Locators
from po_groups_invite_page import GroupsInvitePage_Locators_Base as GroupsInvitePage_Locators
from po_groups_new_page import GroupsNewPage_Locators_Base as GroupsNewPage_Locators
from po_groups_overview_page import GroupsOverviewPage_Locators_Base as GroupsOverviewPage_Locators
from po_groups_page import GroupsPage_Locators_Base as GroupsPage_Locators
from po_groups_wiki_article_page import GroupsWikiArticlePage_Locators_Base as GroupsWikiArticlePage_Locators
from po_groups_wiki_base_page import GroupsWikiBasePage_Locators_Base as GroupsWikiBasePage_Locators
from po_groups_wiki_delete_page import GroupsWikiDeletePage_Locators_Base as GroupsWikiDeletePage_Locators
from po_groups_wiki_edit_page import GroupsWikiEditPage_Locators_Base as GroupsWikiEditPage_Locators
from po_groups_wiki_new_page import GroupsWikiNewPage_Locators_Base as GroupsWikiNewPage_Locators
from po_groups_wiki_rename_page import GroupsWikiRenamePage_Locators_Base as GroupsWikiRenamePage_Locators
from po_hubucoursebase import HubUCourseBasePage_Locators_Base as HubUCourseBasePage_Locators
from po_hubucoursehome import HubUCourseHomePage_Locators_Base as HubUCourseHomePage_Locators
from po_hubucoursemanage import HubUCourseManagePage_Locators_Base as HubUCourseManagePage_Locators
from po_hubucoursemanagedashboard import HubUCourseManageDashboardPage_Locators_Base as HubUCourseManageDashboardPage_Locators
from po_hubucoursemanageemail import HubUCourseManageEmailPage_Locators_Base as HubUCourseManageEmailPage_Locators
from po_hubucoursemanageinvites import HubUCourseManageInvitesPage_Locators_Base as HubUCourseManageInvitesPage_Locators
from po_hubucoursemanagemembership import HubUCourseManageMembershipPage_Locators_Base as HubUCourseManageMembershipPage_Locators
from po_login import LoginPage1_Locators_Base_3 as LoginPage_Locators
from po_loginremind import LoginRemindPage_Locators_Base as LoginRemindPage_Locators
from po_loginreset import LoginResetPage_Locators_Base as LoginResetPage_Locators
from po_members_change_password import MembersChangePasswordPage_Locators_Base as MembersChangePasswordPage_Locators
from po_members_dashboard import MembersDashboardPage_Locators_Base as MembersDashboardPage_Locators
from po_members_profile import MembersProfilePage_Locators_Base as MembersProfilePage_Locators
from po_register import RegisterPage_Locators_Base as RegisterPage_Locators
from po_resources_tool_attachments_page import ResourcesToolAttachmentsPage_Locators_Base as ResourcesToolAttachmentsPage_Locators
from po_resources_tool_contributors_page import ResourcesToolContributorsPage_Locators_Base as ResourcesToolContributorsPage_Locators
from po_resources_tool_description_page import ResourcesToolDescriptionPage_Locators_Base as ResourcesToolDescriptionPage_Locators
from po_resources_tool_finalize_page import ResourcesToolFinalizePage_Locators_Base as ResourcesToolFinalizePage_Locators
from po_resources_tool_tags_page import ResourcesToolTagsPage_Locators_Base as ResourcesToolTagsPage_Locators
from po_resourcespage import ResourcesPage_Locators_Base as ResourcesPage_Locators
from po_resourcesnewattachpage import ResourcesNewAttachPage_Locators_Base as ResourcesNewAttachPage_Locators
from po_resourcesnewauthorspage import ResourcesNewAuthorsPage_Locators_Base as ResourcesNewAuthorsPage_Locators
from po_resourcesnewcomposepage import ResourcesNewComposePage_Locators_Base as ResourcesNewComposePage_Locators
from po_resourcesnewpage import ResourcesNewPage_Locators_Base as ResourcesNewPage_Locators
from po_resourcesnewreviewpage import ResourcesNewReviewPage_Locators_Base as ResourcesNewReviewPage_Locators
from po_resourcesnewtagspage import ResourcesNewTagsPage_Locators_Base as ResourcesNewTagsPage_Locators
from po_support_page import SupportPage_Locators_Base as SupportPage_Locators
from po_supportticketview import SupportTicketViewPage_Locators_Base as SupportTicketViewPage_Locators
from po_supportticketnew import SupportTicketNewPage_Locators_Base as SupportTicketNewPage_Locators
from po_supportticketsave import SupportTicketSavePage_Locators_Base as SupportTicketSavePage_Locators
from po_supportticketsearch import SupportTicketSearchPage2012_Locators_Base as SupportTicketSearchPage2012_Locators
from po_tags_browse_page import TagsBrowsePage_Locators_Base_2 as TagsBrowsePage_Locators
from po_tags_page import TagsPage_Locators_Base as TagsPage_Locators
from po_tags_view_page import TagsViewPage_Locators_Base_2 as TagsViewPage_Locators
from po_time_base_page import TimeBasePage_Locators_Base as TimeBasePage_Locators
from po_time_new_hub_page import TimeNewHubPage_Locators_Base as TimeNewHubPage_Locators
from po_time_new_record_page import TimeNewRecordPage_Locators_Base as TimeNewRecordPage_Locators
from po_time_new_task_page import TimeNewTaskPage_Locators_Base as TimeNewTaskPage_Locators
from po_time_overview_page import TimeOverviewPage_Locators_Base as TimeOverviewPage_Locators
from po_tool_session_page import ToolSessionPage_Locators_Base as ToolSessionPage_Locators
from po_tools_create_page import ToolsCreatePage_Locators_Base as ToolsCreatePage_Locators
from po_tools_pipeline_page import ToolsPipelinePage_Locators_Base as ToolsPipelinePage_Locators
from po_tools_status_approve_confirm_license_page import ToolsStatusApproveConfirmLicensePage_Locators_Base as ToolsStatusApproveConfirmLicensePage_Locators
from po_tools_status_approve_confirm_toolinfo_page import ToolsStatusApproveConfirmToolInfoPage_Locators_Base as ToolsStatusApproveConfirmToolInfoPage_Locators
from po_tools_status_approve_confirm_version_page import ToolsStatusApproveConfirmVersionPage_Locators_Base as ToolsStatusApproveConfirmVersionPage_Locators
from po_tools_status_approved_page import ToolsStatusApprovedPage_Locators_Base as ToolsStatusApprovedPage_Locators
from po_tools_status_base_page import ToolsStatusBasePage_Locators_Base as ToolsStatusBasePage_Locators
from po_tools_status_created_page import ToolsStatusCreatedPage_Locators_Base as ToolsStatusCreatedPage_Locators
from po_tools_status_installed_page import ToolsStatusInstalledPage_Locators_Base as ToolsStatusInstalledPage_Locators
from po_tools_status_published_page import ToolsStatusPublishedPage_Locators_Base as ToolsStatusPublishedPage_Locators
from po_tools_status_registered_page import ToolsStatusRegisteredPage_Locators_Base as ToolsStatusRegisteredPage_Locators
from po_tools_status_uploaded_page import ToolsStatusUploadedPage_Locators_Base as ToolsStatusUploadedPage_Locators
from po_wishlistnewwish import WishlistNewWishPage_Locators_Base as WishlistNewWishPage_Locators
from po_wishlistsearch import WishlistSearchPage_Locators_Base as WishlistSearchPage_Locators


# load widget locators
from widgets.admin_login import AdminLogin1_Locators_Base_1 as AdminLogin_Locators
from widgets.captcha1 import Captcha1_Locators_Base as Captcha1_Locators
from widgets.captcha2 import Captcha2_Locators_Base as Captcha2_Locators
from widgets.courses import Courses_Locators_Base as Courses_Locators
from widgets.dashboard_membership import DashboardMembership_Locators_Base as DashboardMembership_Locators
from widgets.dashboard_tickets import DashboardTickets_Locators_Base as DashboardTickets_Locators
from widgets.footer import Footer_Locators_Base as Footer_Locators
#from widgets.groups import Groups1_Locators_Base_2 as Groups_Locators
from widgets.groups import Groups1_Locators_Base_5 as Groups_Locators
from widgets.groups_customize_form import GroupsCustomizeForm1_Locators_Base as GroupsCustomizeForm
from widgets.groups_delete_form import GroupsDeleteForm_Locators_Base as GroupsDeleteForm_Locators
from widgets.groups_info import GroupsInfo1_Locators_Base as GroupsInfo_Locators
from widgets.groups_invite_form import GroupsInviteForm_Locators_Base as GroupsInviteForm_Locators
from widgets.groups_member_browser import GroupsMemberBrowser_Locators_Base as GroupsMemberBrowser_Locators
from widgets.groups_menu import GroupsMenu1_Locators_Base as GroupsMenu_Locators
from widgets.groups_new_form import GroupsNewForm1_Locators_Base_4 as GroupsNewForm_Locators
from widgets.groups_options import GroupsOptions_Locators_Base as GroupsOptions_Locators
from widgets.groups_overview import GroupsOverview1_Locators_Base as GroupsOverview_Locators
from widgets.groups_title import GroupsTitle_Locators_Base_2 as GroupsTitle_Locators
from widgets.groups_wiki import GroupsWiki_Locators_Base_3 as GroupsWiki_Locators
from widgets.groups_wiki_article import GroupsWikiArticle_Locators_Base as GroupsWikiArticle_Locators
from widgets.groups_wiki_delete_form import GroupsWikiDeleteForm_Locators_Base as GroupsWikiDeleteForm_Locators
from widgets.groups_wiki_edit_form import GroupsWikiEditForm1_Locators_Base as GroupsWikiEditForm_Locators
from widgets.groups_wiki_menu import GroupsWikiMenu1_Locators_Base as GroupsWikiMenu_Locators
from widgets.groups_wiki_new_form import GroupsWikiNewForm1_Locators_Base as GroupsWikiNewForm_Locators
from widgets.groups_wiki_rename_form import GroupsWikiRenameForm_Locators_Base as GroupsWikiRenameForm_Locators
from widgets.header import Header1_Locators_Base_2 as Header_Locators
from widgets.hubu_course_login import HubUCourseLogin_Locators_Base as HubUCourseLogin_Locators
from widgets.hubu_course_manage_emailform import HubUCourseManageEmailForm_Locators_Base as HubUCourseManageEmailForm_Locators
from widgets.hubu_course_manage_tabs import HubUCourseManageTabs_Locators_Base as HubUCourseManageTabs_Locators
from widgets.hubu_course_membership_listing import HubUCourseMembershipListing_Locators_Base as HubUCourseMembershipListing_Locators
from widgets.hubu_course_membership_listing_detail_row import HubUCourseMembershipListingDetailRow_Locators_Base as HubUCourseMembershipListingDetailRow_Locators
from widgets.hubu_course_membership_listing_member_row import HubUCourseMembershipListingMemberRow_Locators_Base as HubUCourseMembershipListingMemberRow_Locators
from widgets.hubu_course_menu import HubUCourseMenu_Locators_Base as HubUCourseMenu_Locators
from widgets.listpagenav import ListPageNav2_Locators_Base as ListPageNav_Locators
from widgets.listtopcounts import ListTopCounts_Locators_Base as ListTopCounts_Locators
from widgets.login_base import Login_Locators_Base_3 as Login_Locators
from widgets.login_remind_form import LoginRemindForm_Locators_Base as LoginRemindForm_Locators
from widgets.login_reset_form import LoginResetForm_Locators_Base as LoginResetForm_Locators
from widgets.members_change_password_form import MembersChangePasswordForm_Locators_Base as MembersChangePasswordForm_Locators
from widgets.members_dashboard_my_sessions import MembersDashboardMySessions_Locators_Base as MembersDashboardMySessions_Locators
from widgets.members_dashboard_my_sessions_item import MembersDashboardMySessionsItem_Locators_Base as MembersDashboardMySessionsItem_Locators
from widgets.members_dashboard_table import MembersDashboardTable1_Locators_Base as MembersDashboardTable_Locators
from widgets.members_pagemenu import MembersPageMenu_Locators_Base as MembersPageMenu_Locators
from widgets.members_profile_biography import MembersProfileBiography_Locators_Base as MembersProfileBiography_Locators
from widgets.members_profile_citizenship import MembersProfileCitizenship_Locators_Base as MembersProfileCitizenship_Locators
from widgets.members_profile_element import MembersProfileElement_Locators_Base as MembersProfileElement_Locators
from widgets.members_profile_email import MembersProfileEmail_Locators_Base as MembersProfileEmail_Locators
from widgets.members_profile_employment import MembersProfileEmployment_Locators_Base as MembersProfileEmployment_Locators
from widgets.members_profile_form import MembersProfileForm_Locators_Base as MembersProfileForm_Locators
from widgets.members_profile_gender import MembersProfileGender_Locators_Base as MembersProfileGender_Locators
from widgets.members_profile_interests import MembersProfileInterests_Locators_Base as MembersProfileInterests_Locators
from widgets.members_profile_mailpreference import MembersProfileMailPreference1_Locators_Base as MembersProfileMailPreference_Locators
from widgets.members_profile_name import MembersProfileName_Locators_Base as MembersProfileName_Locators
from widgets.members_profile_organization import MembersProfileOrganization_Locators_Base as MembersProfileOrganization_Locators
from widgets.members_profile_password import MembersProfilePassword_Locators_Base as MembersProfilePassword_Locators
from widgets.members_profile_residence import MembersProfileResidence_Locators_Base as MembersProfileResidence_Locators
from widgets.members_profile_website import MembersProfileWebsite_Locators_Base as MembersProfileWebsite_Locators
from widgets.members_profile_telephone import MembersProfileTelephone_Locators_Base as MembersProfileTelephone_Locators
from widgets.need_help_form import NeedHelpForm_Locators_Base as NeedHelpForm_Locators
from widgets.popular_item import PopularItem_Locators_Base as PopularItem_Locators
from widgets.register_form import RegisterForm_Locators_Base as RegisterForm_Locators
from widgets.resources import Resources_Locators_Base as Resources_Locators
from widgets.resources_category_browser import ResourcesCategoryBrowser_Locators_Base as ResourcesCategoryBrowser_Locators
from widgets.resources_new import ResourcesNew_Locators_Base as ResourcesNew_Locators
from widgets.resources_new_attach_form import ResourcesNewAttachForm_Locators_Base as ResourcesNewAttachForm_Locators
from widgets.resources_new_authors_authors_list import ResourcesNewAuthorsAuthorsList_Locators_Base as ResourcesNewAuthorsAuthorsList_Locators
from widgets.resources_new_authors_authors_form import ResourcesNewAuthorsAuthorsForm_Locators_Base as ResourcesNewAuthorsAuthorsForm_Locators
from widgets.resources_new_authors_form import ResourcesNewAuthorsForm_Locators_Base as ResourcesNewAuthorsForm_Locators
from widgets.resources_new_compose_form import ResourcesNewComposeForm1_Locators_Base as ResourcesNewComposeForm_Locators
from widgets.resources_new_review_form import ResourcesNewReviewForm_Locators_Base as ResourcesNewReviewForm_Locators
from widgets.resources_new_tags_form import ResourcesNewTagsForm_Locators_Base as ResourcesNewTagsForm_Locators
from widgets.resources_tool_attachments_form import ResourcesToolAttachmentsForm_Locators_Base as ResourcesToolAttachmentsForm_Locators
from widgets.resources_tool_contributors_form import ResourcesToolContributorsForm_Locators_Base as ResourcesToolContributorsForm_Locators
from widgets.resources_tool_description_form import ResourcesToolDescriptionForm1_Locators_Base_1 as ResourcesToolDescriptionForm_Locators
from widgets.resources_tool_file_upload_row import ResourcesToolFileUploadRow_Locators_Base as ResourcesToolFileUploadRow_Locators
from widgets.resources_tool_finalize_form import ResourcesToolFinalizeForm_Locators_Base as ResourcesToolFinalizeForm_Locators
from widgets.resources_tool_screenshot_upload_row import ResourcesToolScreenshotUploadRow_Locators_Base as ResourcesToolScreenshotUploadRow_Locators
from widgets.resources_tool_tags_form import ResourcesToolTagsForm_Locators_Base as ResourcesToolTagsForm_Locators
from widgets.storage_meter import StorageMeter_Locators_Base_2 as StorageMeter_Locators
from widgets.storage_meter import StorageMeter_Locators_Base_2 as MembersDashboardMySessionsStorage_Locators
from widgets.storage_meter import StorageMeter_Locators_Base_2 as ToolSessionAppStorage_Locators
from widgets.support import Support2_Locators_Base as Support_Locators
from widgets.tag_search_box import TagSearchBox_Locators_Base_2 as TagSearchBox_Locators
from widgets.tags import Tags_Locators_Base_1 as Tags_Locators
from widgets.tags_browse_form import TagsBrowseForm_Locators_Base_2 as TagsBrowseForm_Locators
from widgets.tags_browse_order_options import TagsBrowseOrderOptions_Locators_Base as TagsBrowseOrderOptions_Locators
from widgets.tags_browse_results_row import TagsBrowseResultsRow1_Locators_Base_1 as TagsBrowseResultsRow_Locators
from widgets.tags_view_form import TagsViewForm_Locators_Base as TagsViewForm_Locators
from widgets.tags_view_results_row import TagsViewResultsRow_Locators_Base as TagsViewResultsRow_Locators
from widgets.tags_list import TagsList_Locators_Base as TagsList_Locators
from widgets.text_search_box import TextSearchBox_Locators_Base as TextSearchBox_Locators
from widgets.ticket_comment import TicketComment_Locators_Base_2 as TicketComment_Locators
from widgets.ticket_comment_base import TicketCommentBase_Locators_Base as TicketCommentBase_Locators
from widgets.ticket_comment_form import TicketCommentForm_Locators_Base as TicketCommentForm_Locators
from widgets.ticket_comment_list import TicketCommentList_Locators_Base as TicketCommentList_Locators
from widgets.ticket_content import TicketContent_Locators_Base_2 as TicketContent_Locators
from widgets.ticket_list_filter_options import TicketListFilterOptions_Locators_Base as TicketListFilterOptions_Locators
from widgets.ticket_list_search_form import TicketListSearchForm_Locators_Base as TicketListSearchForm_Locators
from widgets.ticket_list_search_result_row import TicketListSearchResultRow_Locators_Base_2 as TicketListSearchResultRow_Locators
from widgets.ticket_list_sort_options import TicketListSortOptions_Locators_Base as TicketListSortOptions_Locators
from widgets.ticket_new_form import TicketNewForm_Locators_Base as TicketNewForm_Locators
from widgets.ticket_save import TicketSave_Locators_Base_3 as TicketSave_Locators
from widgets.time_navigation import TimeNavigation_Locators_Base as TimeNavigation_Locators
from widgets.time_new_hub_form import TimeNewHubForm_Locators_Base as TimeNewHubForm_Locators
from widgets.time_new_record_form import TimeNewRecordForm_Locators_Base as TimeNewRecordForm_Locators
from widgets.time_new_task_form import TimeNewTaskForm_Locators_Base as TimeNewTaskForm_Locators
from widgets.time_overview import TimeOverview_Locators_Base as TimeOverview_Locators
from widgets.tool_session_app import ToolSessionApp_Locators_Base as ToolSessionApp_Locators
from widgets.tool_session_share import ToolSessionShare_Locators_Base as ToolSessionShare_Locators
from widgets.tool_session_shared_with_item import ToolSessionSharedWithItem_Locators_Base as ToolSessionSharedWithItem_Locators
from widgets.tools_create_form import ToolsCreateForm_Locators_Base as ToolsCreateForm_Locators
from widgets.tools_pipeline_filter_options import ToolsPipelineFilterOptions_Locators_Base_2 as ToolsPipelineFilterOptions_Locators
from widgets.tools_pipeline_search_form import ToolsPipelineSearchForm_Locators_Base as ToolsPipelineSearchForm_Locators
from widgets.tools_pipeline_search_result_row import ToolsPipelineSearchResultRow_Locators_Base as ToolsPipelineSearchResultRow_Locators
from widgets.tools_pipeline_sort_options import ToolsPipelineSortOptions_Locators_Base_2 as ToolsPipelineSortOptions_Locators
from widgets.tools_status_administrator_controls import ToolsStatusAdministratorControls_Locators_Base as ToolsStatusAdministratorControls_Locators
from widgets.tools_status_administrator_form import ToolsStatusAdministratorForm_Locators_Base as ToolsStatusAdministratorForm_Locators
from widgets.tools_status_approve_license_form import ToolsStatusApproveLicenseForm_Locators_Base as ToolsStatusApproveLicenseForm_Locators
from widgets.tools_status_approve_toolinfo_form import ToolsStatusApproveToolInfoForm_Locators_Base as ToolsStatusApproveToolInfoForm_Locators
from widgets.tools_status_approve_version_form import ToolsStatusApproveVersionForm_Locators_Base as ToolsStatusApproveVersionForm_Locators
from widgets.tools_status_approved import ToolsStatusApproved_Locators_Base as ToolsStatusApproved_Locators
from widgets.tools_status_base import ToolsStatusBase_Locators_Base as ToolsStatusBase_Locators
from widgets.tools_status_created import ToolsStatusCreated_Locators_Base as ToolsStatusCreated_Locators
from widgets.tools_status_developer_tools import ToolsStatusDeveloperTools_Locators_Base as ToolsStatusDeveloperTools_Locators
from widgets.tools_status_installed import ToolsStatusInstalled_Locators_Base as ToolsStatusInstalled_Locators
from widgets.tools_status_published import ToolsStatusPublished_Locators_Base as ToolsStatusPublished_Locators
from widgets.tools_status_registered import ToolsStatusRegistered_Locators_Base as ToolsStatusRegistered_Locators
from widgets.tools_status_remaining_steps import ToolsStatusRemainingSteps_Locators_Base as ToolsStatusRemainingSteps_Locators
from widgets.tools_status_tool_info import ToolsStatusToolInfo_Locators_Base as ToolsStatusToolInfo_Locators
from widgets.tools_status_uploaded import ToolsStatusUploaded_Locators_Base as ToolsStatusUploaded_Locators
from widgets.tools_status_whats_next_approved import ToolsStatusWhatsNextApproved_Locators_Base as ToolsStatusWhatsNextApproved_Locators
from widgets.tools_status_whats_next_created import ToolsStatusWhatsNextCreated_Locators_Base as ToolsStatusWhatsNextCreated_Locators
from widgets.tools_status_whats_next_installed import ToolsStatusWhatsNextInstalled_Locators_Base as ToolsStatusWhatsNextInstalled_Locators
from widgets.tools_status_whats_next_published import ToolsStatusWhatsNextPublished_Locators_Base as ToolsStatusWhatsNextPublished_Locators
from widgets.tools_status_whats_next_registered import ToolsStatusWhatsNextRegistered_Locators_Base as ToolsStatusWhatsNextRegistered_Locators
from widgets.tools_status_whats_next_uploaded import ToolsStatusWhatsNextUploaded_Locators_Base as ToolsStatusWhatsNextUploaded_Locators
from widgets.tools_status_version_list_row import ToolsStatusVersionListRow_Locators_Base as ToolsStatusVersionListRow_Locators
from widgets.trouble_report_form import TroubleReportForm_Locators_Base as TroubleReportForm_Locators
from widgets.upload2 import Upload2_Locators_Base as Upload2_Locators
from widgets.upload_list1 import UploadList1_Locators_Base as UploadList1_Locators
from widgets.upload_list2 import UploadList2_Locators_Base_2 as UploadList2_Locators
from widgets.wiki_text_area import WikiTextArea_Locators_Base as WikiTextArea_Locators
from widgets.wishlist_search_form import WishlistSearchForm_Locators_Base as WishlistSearchForm_Locators
from widgets.wishlist_filter_options import WishlistFilterOptions_Locators_Base as WishlistFilterOptions_Locators
from widgets.wishlist_new_wish_form import WishlistNewWishForm_Locators_Base as WishlistNewWishForm_Locators
from widgets.wishlist_order_options import WishlistOrderOptions_Locators_Base as WishlistOrderOptions_Locators
from widgets.wishlist_search_result_row import WishlistSearchResultRow_Locators_Base as WishlistSearchResultRow_Locators
from widgets.wishlist_search_result_row_detail import WishlistSearchResultRowDetail_Locators_Base as WishlistSearchResultRowDetail_Locators
from widgets.wishlist_vote import WishlistVote_Locators_Base as WishlistVote_Locators
