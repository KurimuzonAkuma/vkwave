import typing
from enum import Enum

import pydantic


class AccountNameRequestStatus(Enum):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AccountNameRequestStatus.CANNOT_BE_REPRESENTED


class AccountPushParamsMode(Enum):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AccountPushParamsMode.CANNOT_BE_REPRESENTED


class AccountPushParamsOnoff(Enum):
    ON = "on"
    OFF = "off"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AccountPushParamsOnoff.CANNOT_BE_REPRESENTED


class AccountPushParamsSettings(Enum):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AccountPushParamsSettings.CANNOT_BE_REPRESENTED


class AddressesFields(Enum):
    ID = "id"
    TITLE = "title"
    ADDRESS = "address"
    ADDITIONAL_ADDRESS = "additional_address"
    COUNTRY_ID = "country_id"
    CITY_ID = "city_id"
    METRO_STATION_ID = "metro_station_id"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    DISTANCE = "distance"
    WORK_INFO_STATUS = "work_info_status"
    TIMETABLE = "timetable"
    PHONE = "phone"
    TIME_OFFSET = "time_offset"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AddressesFields.CANNOT_BE_REPRESENTED


class AdsAccessRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsAccessRole.CANNOT_BE_REPRESENTED


class AdsAccessRolePublic(Enum):
    MANAGER = "manager"
    REPORTS = "reports"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsAccessRolePublic.CANNOT_BE_REPRESENTED


class AdsAccountType(Enum):
    GENERAL = "general"
    AGENCY = "agency"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsAccountType.CANNOT_BE_REPRESENTED


class AdsAdApproved(Enum):
    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsAdApproved.CANNOT_BE_REPRESENTED


class AdsAdCostType(Enum):
    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsAdCostType.CANNOT_BE_REPRESENTED


class AdsAdStatus(Enum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsAdStatus.CANNOT_BE_REPRESENTED


class AdsCampaignStatus(Enum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsCampaignStatus.CANNOT_BE_REPRESENTED


class AdsCampaignType(Enum):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsCampaignType.CANNOT_BE_REPRESENTED


class AdsCriteriaSex(Enum):
    ANY = 0
    MALE = 1
    FEMALE = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsCriteriaSex.CANNOT_BE_REPRESENTED


class AdsObjectType(Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsObjectType.CANNOT_BE_REPRESENTED


class AdsStatsSexValue(Enum):
    F = "f"
    M = "m"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsStatsSexValue.CANNOT_BE_REPRESENTED


class AdsTargSuggestionsSchoolsType(Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AdsTargSuggestionsSchoolsType.CANNOT_BE_REPRESENTED


class AppsAppLeaderboardType(Enum):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AppsAppLeaderboardType.CANNOT_BE_REPRESENTED


class AppsAppType(Enum):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return AppsAppType.CANNOT_BE_REPRESENTED


class BaseBoolInt(Enum):
    NO = 0
    YES = 1
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BaseBoolInt.CANNOT_BE_REPRESENTED


class BaseLinkButtonActionType(Enum):
    OPEN_URL = "open_url"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BaseLinkButtonActionType.CANNOT_BE_REPRESENTED


class BaseLinkButtonStyle(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BaseLinkButtonStyle.CANNOT_BE_REPRESENTED


class BaseLinkProductStatus(Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BaseLinkProductStatus.CANNOT_BE_REPRESENTED


class BasePropertyExists(Enum):
    PROPERTY_EXISTS = 1
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BasePropertyExists.CANNOT_BE_REPRESENTED


class BaseSex(Enum):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BaseSex.CANNOT_BE_REPRESENTED


class BaseUserGroupFields(Enum):
    ABOUT = "about"
    ACTION_BUTTON = "action_button"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    ADDRESSES = "addresses"
    ADMIN_LEVEL = "admin_level"
    AGE_LIMITS = "age_limits"
    AUTHOR_ID = "author_id"
    BAN_INFO = "ban_info"
    BDATE = "bdate"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    BOOKS = "books"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_MESSAGE = "can_message"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAREER = "career"
    CITY = "city"
    COMMON_COUNT = "common_count"
    CONNECTIONS = "connections"
    CONTACTS = "contacts"
    COUNTERS = "counters"
    COUNTRY = "country"
    COVER = "cover"
    CROP_PHOTO = "crop_photo"
    DEACTIVATED = "deactivated"
    DESCRIPTION = "description"
    DOMAIN = "domain"
    EDUCATION = "education"
    EXPORTS = "exports"
    FINISH_DATE = "finish_date"
    FIXED_POST = "fixed_post"
    FOLLOWERS_COUNT = "followers_count"
    FRIEND_STATUS = "friend_status"
    GAMES = "games"
    HAS_MARKET_APP = "has_market_app"
    HAS_MOBILE = "has_mobile"
    HAS_PHOTO = "has_photo"
    HOME_TOWN = "home_town"
    ID = "id"
    INTERESTS = "interests"
    IS_ADMIN = "is_admin"
    IS_CLOSED = "is_closed"
    IS_FAVORITE = "is_favorite"
    IS_FRIEND = "is_friend"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_MEMBER = "is_member"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    IS_SUBSCRIBED = "is_subscribed"
    LAST_SEEN = "last_seen"
    LINKS = "links"
    LISTS = "lists"
    MAIDEN_NAME = "maiden_name"
    MAIN_ALBUM_ID = "main_album_id"
    MAIN_SECTION = "main_section"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    MEMBERS_COUNT = "members_count"
    MILITARY = "military"
    MOVIES = "movies"
    MUSIC = "music"
    NAME = "name"
    NICKNAME = "nickname"
    OCCUPATION = "occupation"
    ONLINE = "online"
    ONLINE_STATUS = "online_status"
    PERSONAL = "personal"
    PHONE = "phone"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_50 = "photo_50"
    PHOTO_ID = "photo_id"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    QUOTES = "quotes"
    RELATION = "relation"
    RELATIVES = "relatives"
    SCHOOLS = "schools"
    SCREEN_NAME = "screen_name"
    SEX = "sex"
    SITE = "site"
    START_DATE = "start_date"
    STATUS = "status"
    TIMEZONE = "timezone"
    TRENDING = "trending"
    TV = "tv"
    TYPE = "type"
    UNIVERSITIES = "universities"
    VERIFIED = "verified"
    WALL_COMMENTS = "wall_comments"
    WIKI_PAGE = "wiki_page"
    VK_ADMIN_STATUS = "vk_admin_status"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BaseUserGroupFields.CANNOT_BE_REPRESENTED


class BoardDefaultOrder(Enum):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return BoardDefaultOrder.CANNOT_BE_REPRESENTED


class CallbackGroupJoinType(Enum):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return CallbackGroupJoinType.CANNOT_BE_REPRESENTED


class CallbackGroupMarket(Enum):
    DISABLED = 0
    OPEN = 1
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return CallbackGroupMarket.CANNOT_BE_REPRESENTED


class CallbackGroupOfficerRole(Enum):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return CallbackGroupOfficerRole.CANNOT_BE_REPRESENTED


class CallbackMessageType(Enum):
    CONFIRMATION = "confirmation"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return CallbackMessageType.CANNOT_BE_REPRESENTED


class DocsDocAttachmentType(Enum):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return DocsDocAttachmentType.CANNOT_BE_REPRESENTED


class FaveBookmarkType(Enum):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return FaveBookmarkType.CANNOT_BE_REPRESENTED


class FavePageType(Enum):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return FavePageType.CANNOT_BE_REPRESENTED


class FriendsFriendStatusStatus(Enum):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return FriendsFriendStatusStatus.CANNOT_BE_REPRESENTED


class GiftsGiftPrivacy(Enum):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GiftsGiftPrivacy.CANNOT_BE_REPRESENTED


class GroupsAddressWorkInfoStatus(Enum):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsAddressWorkInfoStatus.CANNOT_BE_REPRESENTED


class GroupsBanInfoReason(Enum):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsBanInfoReason.CANNOT_BE_REPRESENTED


class GroupsFields(Enum):
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    CITY = "city"
    COUNTRY = "country"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    HAS_PHOTO = "has_photo"
    STATUS = "status"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    SITE = "site"
    MAIN_SECTION = "main_section"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    ONLINE_STATUS = "online_status"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    ACTION_BUTTON = "action_button"
    AUTHOR_ID = "author_id"
    PHONE = "phone"
    HAS_MARKET_APP = "has_market_app"
    ADDRESSES = "addresses"
    LIVE_COVERS = "live_covers"
    IS_ADULT = "is_adult"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    WARNING_NOTIFICATION = "warning_notification"
    MSG_PUSH_ALLOWED = "msg_push_allowed"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsFields.CANNOT_BE_REPRESENTED


class GroupsFilter(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsFilter.CANNOT_BE_REPRESENTED


class GroupsGroupAccess(Enum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupAccess.CANNOT_BE_REPRESENTED


class GroupsGroupAdminLevel(Enum):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupAdminLevel.CANNOT_BE_REPRESENTED


class GroupsGroupAgeLimits(Enum):
    UNLIMITED = 1
    SIXTEEN_PLUS = 2
    EIGHTEEN_PLUS = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupAgeLimits.CANNOT_BE_REPRESENTED


class GroupsGroupAudio(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupAudio.CANNOT_BE_REPRESENTED


class GroupsGroupDocs(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupDocs.CANNOT_BE_REPRESENTED


class GroupsGroupFullAgeLimits(Enum):
    NO = 1
    OVER_SIXTEEN = 2
    OVER_EIGHTEEN = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupFullAgeLimits.CANNOT_BE_REPRESENTED


class GroupsGroupFullMainSection(Enum):
    ABSENT = 0
    PHOTOS = 1
    TOPICS = 2
    AUDIO = 3
    VIDEO = 4
    MARKET = 5
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupFullMainSection.CANNOT_BE_REPRESENTED


class GroupsGroupFullMemberStatus(Enum):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupFullMemberStatus.CANNOT_BE_REPRESENTED


class GroupsGroupIsClosed(Enum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupIsClosed.CANNOT_BE_REPRESENTED


class GroupsGroupMarketCurrency(Enum):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupMarketCurrency.CANNOT_BE_REPRESENTED


class GroupsGroupPhotos(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupPhotos.CANNOT_BE_REPRESENTED


class GroupsGroupRole(Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupRole.CANNOT_BE_REPRESENTED


class GroupsGroupSubject(Enum):
    AUTO = 1
    ACTIVITY_HOLIDAYS = 2
    BUSINESS = 3
    PETS = 4
    HEALTH = 5
    DATING_AND_COMMUNICATION = 6
    GAMES = 7
    IT = 8
    CINEMA = 9
    BEAUTY_AND_FASHION = 10
    COOKING = 11
    ART_AND_CULTURE = 12
    LITERATURE = 13
    MOBILE_SERVICES_AND_INTERNET = 14
    MUSIC = 15
    SCIENCE_AND_TECHNOLOGY = 16
    REAL_ESTATE = 17
    NEWS_AND_MEDIA = 18
    SECURITY = 19
    EDUCATION = 20
    HOME_AND_RENOVATIONS = 21
    POLITICS = 22
    FOOD = 23
    INDUSTRY = 24
    TRAVEL = 25
    WORK = 26
    ENTERTAINMENT = 27
    RELIGION = 28
    FAMILY = 29
    SPORTS = 30
    INSURANCE = 31
    TELEVISION = 32
    GOODS_AND_SERVICES = 33
    HOBBIES = 34
    FINANCE = 35
    PHOTO = 36
    ESOTERICS = 37
    ELECTRONICS_AND_APPLIANCES = 38
    EROTIC = 39
    HUMOR = 40
    SOCIETY_HUMANITIES = 41
    DESIGN_AND_GRAPHICS = 42
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupSubject.CANNOT_BE_REPRESENTED


class GroupsGroupTopics(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupTopics.CANNOT_BE_REPRESENTED


class GroupsGroupType(Enum):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupType.CANNOT_BE_REPRESENTED


class GroupsGroupVideo(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupVideo.CANNOT_BE_REPRESENTED


class GroupsGroupWall(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupWall.CANNOT_BE_REPRESENTED


class GroupsGroupWiki(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupWiki.CANNOT_BE_REPRESENTED


class GroupsGroupXtrInvitedByAdminLevel(Enum):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupXtrInvitedByAdminLevel.CANNOT_BE_REPRESENTED


class GroupsGroupXtrInvitedByType(Enum):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsGroupXtrInvitedByType.CANNOT_BE_REPRESENTED


class GroupsMarketState(Enum):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsMarketState.CANNOT_BE_REPRESENTED


class GroupsMemberRolePermission(Enum):
    ADS = "ads"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsMemberRolePermission.CANNOT_BE_REPRESENTED


class GroupsMemberRoleStatus(Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsMemberRoleStatus.CANNOT_BE_REPRESENTED


class GroupsOnlineStatusType(Enum):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsOnlineStatusType.CANNOT_BE_REPRESENTED


class GroupsOwnerXtrBanInfoType(Enum):
    GROUP = "group"
    PROFILE = "profile"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsOwnerXtrBanInfoType.CANNOT_BE_REPRESENTED


class GroupsRoleOptions(Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return GroupsRoleOptions.CANNOT_BE_REPRESENTED


class LikesType(Enum):
    POST = "post"
    COMMENT = "comment"
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    NOTE = "note"
    MARKET = "market"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    TOPIC_COMMENT = "topic_comment"
    MARKET_COMMENT = "market_comment"
    SITEPAGE = "sitepage"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return LikesType.CANNOT_BE_REPRESENTED


class MarketMarketItemAvailability(Enum):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return MarketMarketItemAvailability.CANNOT_BE_REPRESENTED


class MessagesConversationPeerType(Enum):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return MessagesConversationPeerType.CANNOT_BE_REPRESENTED


class MessagesHistoryMessageAttachmentType(Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    WALL = "wall"
    SHARE = "share"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return MessagesHistoryMessageAttachmentType.CANNOT_BE_REPRESENTED


class MessagesMessageActionStatus(Enum):
    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"
    CHAT_INVITE_USER_BY_MESSAGE_REQUEST = "chat_invite_user_by_message_request"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return MessagesMessageActionStatus.CANNOT_BE_REPRESENTED


class MessagesMessageAttachmentType(Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"
    POLL = "poll"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return MessagesMessageAttachmentType.CANNOT_BE_REPRESENTED


class MessagesTemplateActionTypeNames(Enum):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return MessagesTemplateActionTypeNames.CANNOT_BE_REPRESENTED


class NewsfeedCommentsFilters(Enum):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return NewsfeedCommentsFilters.CANNOT_BE_REPRESENTED


class NewsfeedFilters(Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    RECOMMENDED_GROUPS = "recommended_groups"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    AUDIO_PLAYLIST = "audio_playlist"
    GAMES_CAROUSEL = "games_carousel"
    CLIP = "clip"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return NewsfeedFilters.CANNOT_BE_REPRESENTED


class NewsfeedIgnoreItemType(Enum):
    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return NewsfeedIgnoreItemType.CANNOT_BE_REPRESENTED


class NewsfeedItemWallpostFeedbackType(Enum):
    BUTTONS = "buttons"
    STARS = "stars"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return NewsfeedItemWallpostFeedbackType.CANNOT_BE_REPRESENTED


class NewsfeedItemWallpostType(Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return NewsfeedItemWallpostType.CANNOT_BE_REPRESENTED


class NewsfeedNewsfeedItemType(Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return NewsfeedNewsfeedItemType.CANNOT_BE_REPRESENTED


class NotificationsNotificationItem(Enum):
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return NotificationsNotificationItem.CANNOT_BE_REPRESENTED


class PagesPrivacySettings(Enum):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return PagesPrivacySettings.CANNOT_BE_REPRESENTED


class PhotosImageType(Enum):
    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return PhotosImageType.CANNOT_BE_REPRESENTED


class PhotosPhotoSizesType(Enum):
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"
    A = "a"
    B = "b"
    E = "e"
    I = "i"
    D = "d"
    J = "j"
    TEMP = "temp"
    H = "h"
    G = "g"
    N = "n"
    F = "f"
    MAX = "max"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return PhotosPhotoSizesType.CANNOT_BE_REPRESENTED


class SearchHintSection(Enum):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return SearchHintSection.CANNOT_BE_REPRESENTED


class SearchHintType(Enum):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return SearchHintType.CANNOT_BE_REPRESENTED


class StoriesStoryStatsState(Enum):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return StoriesStoryStatsState.CANNOT_BE_REPRESENTED


class StoriesStoryType(Enum):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    BIRTHDAY_INVITE = "birthday_invite"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return StoriesStoryType.CANNOT_BE_REPRESENTED


class StoriesUploadLinkText(Enum):
    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return StoriesUploadLinkText.CANNOT_BE_REPRESENTED


class UsersFields(Enum):
    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    CITY = "city"
    COUNTRY = "country"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    PHOTO_MAX_SIZE = "photo_max_size"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    ACTIVITIES = "activities"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    SERVICE_DESCRIPTION = "service_description"
    IS_DEAD = "is_dead"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return UsersFields.CANNOT_BE_REPRESENTED


class UsersUserRelation(Enum):
    NOT_SPECIFIED = 0
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    COMPLICATED = 5
    ACTIVELY_SEARCHING = 6
    IN_LOVE = 7
    IN_A_CIVIL_UNION = 8
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return UsersUserRelation.CANNOT_BE_REPRESENTED


class UsersUserType(Enum):
    PROFILE = "profile"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return UsersUserType.CANNOT_BE_REPRESENTED


class UtilsDomainResolvedType(Enum):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return UtilsDomainResolvedType.CANNOT_BE_REPRESENTED


class UtilsLinkCheckedStatus(Enum):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return UtilsLinkCheckedStatus.CANNOT_BE_REPRESENTED


class WallCommentAttachmentType(Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return WallCommentAttachmentType.CANNOT_BE_REPRESENTED


class WallPostSourceType(Enum):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return WallPostSourceType.CANNOT_BE_REPRESENTED


class WallPostType(Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return WallPostType.CANNOT_BE_REPRESENTED


class WallWallpostAttachmentType(Enum):
    PHOTO = "photo"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    PHOTOS_LIST = "photos_list"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    EVENT = "event"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return WallWallpostAttachmentType.CANNOT_BE_REPRESENTED


class WidgetsCommentMediaType(Enum):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"
    CANNOT_BE_REPRESENTED = "CANNOT_BE_REPRESENTED"

    @classmethod
    def _missing_(cls, value):
        return WidgetsCommentMediaType.CANNOT_BE_REPRESENTED


class AccountNameRequest(pydantic.BaseModel):
    first_name: typing.Optional[str] = pydantic.Field(
        None,
        description="First name in request",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Request ID needed to cancel the request",
    )
    last_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Last name in request",
    )
    status: typing.Optional["AccountNameRequestStatus"] = pydantic.Field(
        None,
        description="",
    )
    lang: typing.Optional[str] = pydantic.Field(
        None,
        description="Text to display to user",
    )
    link_href: typing.Optional[str] = pydantic.Field(
        None,
        description="href for link in lang field",
    )
    link_label: typing.Optional[str] = pydantic.Field(
        None,
        description="label to display for link in lang field",
    )


class AccountPushConversations(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Items count",
    )
    items: typing.Optional[typing.List["AccountPushConversationsItem"]] = pydantic.Field(
        None,
        description="",
    )


class AccountPushParams(pydantic.BaseModel):
    msg: typing.Optional[typing.List["AccountPushParamsMode"]] = pydantic.Field(
        None,
        description="",
    )
    chat: typing.Optional[typing.List["AccountPushParamsMode"]] = pydantic.Field(
        None,
        description="",
    )
    like: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None,
        description="",
    )
    repost: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None,
        description="",
    )
    comment: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None,
        description="",
    )
    mention: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None,
        description="",
    )
    reply: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    new_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    wall_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    wall_publish: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    friend: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    friend_found: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    friend_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    group_invite: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    group_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    birthday: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    event_soon: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    app_request: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )
    sdk_open: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None,
        description="",
    )


class AccountUserSettingsInterest(pydantic.BaseModel):
    title: str = pydantic.Field(
        ...,
        description="",
    )
    value: str = pydantic.Field(
        ...,
        description="",
    )


class AccountUserSettingsInterests(pydantic.BaseModel):
    activities: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    interests: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    music: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    tv: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    movies: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    books: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    games: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    quotes: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )
    about: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None,
        description="",
    )


class AdsDemostatsFormat(pydantic.BaseModel):
    age: typing.Optional[typing.List["AdsStatsAge"]] = pydantic.Field(
        None,
        description="",
    )
    cities: typing.Optional[typing.List["AdsStatsCities"]] = pydantic.Field(
        None,
        description="",
    )
    day: typing.Optional[str] = pydantic.Field(
        None,
        description="Day as YYYY-MM-DD",
    )
    month: typing.Optional[str] = pydantic.Field(
        None,
        description="Month as YYYY-MM",
    )
    overall: typing.Optional[int] = pydantic.Field(
        None,
        description="1 if period=overall",
    )
    sex: typing.Optional[typing.List["AdsStatsSex"]] = pydantic.Field(
        None,
        description="",
    )
    sex_age: typing.Optional[typing.List["AdsStatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )


class AdsStatsFormat(pydantic.BaseModel):
    clicks: typing.Optional[int] = pydantic.Field(
        None,
        description="Clicks number",
    )
    day: typing.Optional[str] = pydantic.Field(
        None,
        description="Day as YYYY-MM-DD",
    )
    impressions: typing.Optional[int] = pydantic.Field(
        None,
        description="Impressions number",
    )
    join_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Events number",
    )
    month: typing.Optional[str] = pydantic.Field(
        None,
        description="Month as YYYY-MM",
    )
    overall: typing.Optional[int] = pydantic.Field(
        None,
        description="1 if period=overall",
    )
    reach: typing.Optional[int] = pydantic.Field(
        None,
        description="Reach ",
    )
    spent: typing.Optional[int] = pydantic.Field(
        None,
        description="Spent funds",
    )
    video_clicks_site: typing.Optional[int] = pydantic.Field(
        None,
        description="Clickthoughs to the advertised site",
    )
    video_views: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views number",
    )
    video_views_full: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views (full video)",
    )
    video_views_half: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views (half of video)",
    )


class AdsStatsViewsTimes(pydantic.BaseModel):
    views_ads_times_1: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_2: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_3: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_4: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_5: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_6: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_7: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_8: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_9: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_10: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    views_ads_times_11_plus: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class AppsAppMin(pydantic.BaseModel):
    type: "AppsAppType" = pydantic.Field(
        ...,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="Application ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Application title",
    )
    author_owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Application author's ID",
    )
    is_installed: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is application installed",
    )
    icon_139: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app icon with 139 px in width",
    )
    icon_150: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app icon with 150 px in width",
    )
    icon_278: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app icon with 278 px in width",
    )
    icon_576: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app icon with 576 px in width",
    )
    background_loader_color: typing.Optional[str] = pydantic.Field(
        None,
        description="Hex color code without hash sign",
    )
    loader_icon: typing.Optional[str] = pydantic.Field(
        None,
        description="SVG data",
    )
    icon_75: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app icon with 75 px in width",
    )


class AudioAds(pydantic.BaseModel):
    content_id: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    duration: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    account_age_type: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    puid1: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    puid22: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class AudioAlbumThumb(pydantic.BaseModel):
    width: int = pydantic.Field(
        ...,
        description="",
    )
    height: int = pydantic.Field(
        ...,
        description="",
    )
    photo_34: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_68: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_135: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_270: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_300: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_600: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_1200: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class AudioAlbum(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Album ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Title",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Owner ID",
    )
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    thumb: typing.Optional["AudioAlbumThumb"] = pydantic.Field(
        None,
        description=""
    )


class AudioArtist(pydantic.BaseModel):
    name: str = pydantic.Field(
        ...,
        description="Artist name",
    )
    domain: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    id: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class AudioAudio(pydantic.BaseModel):
    artist: str = pydantic.Field(
        ...,
        description="Artist name",
    )
    id: int = pydantic.Field(
        ...,
        description="Audio ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Title",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="""
        URL of :
            1) direct mp3 for old songs, old tokens (not determined exactly)
            2) HLS playlist with link that can be transformed to direct mp3
            3) HLS playlist with link that can not be transformed to direct mp3 (not determined exactly)
        """,
    )
    duration: int = pydantic.Field(
        ...,
        description="Duration in seconds",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when uploaded",
    )
    album_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Album ID",
    )
    genre_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Genre ID",
    )
    performer: typing.Optional[str] = pydantic.Field(
        None,
        description="Performer name",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Owner ID",
    )
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    is_explicit: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    is_focus_track: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    is_licensed: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    track_code: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    short_videos_allowed: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    stories_cover_allowed: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    stories_allowed: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    ads: typing.Optional["AudioAds"] = pydantic.Field(
        None,
        description="",
    )
    album: typing.Optional["AudioAlbum"] = pydantic.Field(
        None,
        description="",
    )
    main_artists: typing.Optional[typing.List["AudioArtist"]] = pydantic.Field(
        None,
        description="",
    )


class BaseCity(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="City ID",
    )
    title: str = pydantic.Field(
        ...,
        description="City title",
    )


class BaseCommentsInfo(pydantic.BaseModel):
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the post",
    )
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Comments number",
    )
    groups_can_post: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether groups can comment the post",
    )
    donut: typing.Optional["WallWallpostCommentsDonut"] = pydantic.Field(
        None,
        description="",
    )


class BaseCountry(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Country ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Country title",
    )


class BaseCropPhotoCrop(pydantic.BaseModel):
    x: int = pydantic.Field(
        ...,
        description="Coordinate X of the left upper corner",
    )
    y: int = pydantic.Field(
        ...,
        description="Coordinate Y of the left upper corner",
    )
    x2: int = pydantic.Field(
        ...,
        description="Coordinate X of the right lower corner",
    )
    y2: int = pydantic.Field(
        ...,
        description="Coordinate Y of the right lower corner",
    )


class BaseCropPhotoRect(pydantic.BaseModel):
    x: int = pydantic.Field(
        ...,
        description="Coordinate X of the left upper corner",
    )
    y: int = pydantic.Field(
        ...,
        description="Coordinate Y of the left upper corner",
    )
    x2: int = pydantic.Field(
        ...,
        description="Coordinate X of the right lower corner",
    )
    y2: int = pydantic.Field(
        ...,
        description="Coordinate Y of the right lower corner",
    )


class BaseError(pydantic.BaseModel):
    error_code: typing.Optional[int] = pydantic.Field(
        None,
        description="Error code",
    )
    error_subcode: typing.Optional[int] = pydantic.Field(
        None,
        description="Error subcode",
    )
    error_msg: typing.Optional[str] = pydantic.Field(
        None,
        description="Error message",
    )
    error_text: typing.Optional[str] = pydantic.Field(
        None,
        description="Localized error message",
    )
    request_params: typing.Optional[typing.List["BaseRequestParam"]] = pydantic.Field(
        None,
        description="",
    )


class BaseGeo(pydantic.BaseModel):
    coordinates: typing.Optional["BaseGeoCoordinates"] = pydantic.Field(
        None,
        description="",
    )
    place: typing.Optional["BasePlace"] = pydantic.Field(
        None,
        description="",
    )
    showmap: typing.Optional[int] = pydantic.Field(
        None,
        description="Information whether a map is showed",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Place type",
    )


class BaseGeoCoordinates(pydantic.BaseModel):
    latitude: float = pydantic.Field(
        ...,
        description="",
    )
    longitude: float = pydantic.Field(
        ...,
        description="",
    )


class BaseLikes(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Likes number",
    )
    user_likes: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user likes the photo",
    )


class BaseLikesInfo(pydantic.BaseModel):
    can_like: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can like the post",
    )
    can_publish: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can repost",
    )
    count: int = pydantic.Field(
        ...,
        description="Likes number",
    )
    user_likes: typing.Optional[int] = pydantic.Field(
        None,
        description="Information whether current uer has liked the post",
    )


class BaseLink(pydantic.BaseModel):
    application: typing.Optional["BaseLinkApplication"] = pydantic.Field(
        None,
        description="",
    )
    button: typing.Optional["BaseLinkButton"] = pydantic.Field(
        None,
        description="",
    )
    caption: typing.Optional[str] = pydantic.Field(
        None,
        description="Link caption",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Link description",
    )
    id: typing.Optional[str] = pydantic.Field(
        None,
        description="Link ID",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    preview_page: typing.Optional[str] = pydantic.Field(
        None,
        description="String ID of the page with article preview",
    )
    preview_url: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the page with article preview",
    )
    product: typing.Optional["BaseLinkProduct"] = pydantic.Field(
        None,
        description="",
    )
    rating: typing.Optional["BaseLinkRating"] = pydantic.Field(
        None,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Link title",
    )
    url: str = pydantic.Field(
        ...,
        description="Link URL",
    )
    target_object: typing.Optional["LinkTargetObject"] = pydantic.Field(
        None,
        description="",
    )
    is_external: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the current link is external",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="Video from link",
    )


class BaseLinkApplication(pydantic.BaseModel):
    app_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Application Id",
    )
    store: typing.Optional["BaseLinkApplicationStore"] = pydantic.Field(
        None,
        description="",
    )


class BaseLinkApplicationStore(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Store Id",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Store name",
    )


class BaseLinkButton(pydantic.BaseModel):
    action: typing.Optional["BaseLinkButtonAction"] = pydantic.Field(
        None,
        description="Button action",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Button title",
    )
    block_id: typing.Optional[str] = pydantic.Field(
        None,
        description="Target block id",
    )
    section_id: typing.Optional[str] = pydantic.Field(
        None,
        description="Target section id",
    )
    curator_id: typing.Optional[int] = pydantic.Field(
        None,
        description="curator id",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Owner id",
    )
    icon: typing.Optional[str] = pydantic.Field(
        None,
        description="Button icon name, e.g. 'phone' or 'gift'",
    )
    style: typing.Optional["BaseLinkButtonStyle"] = pydantic.Field(
        None,
        description="",
    )


class BaseLinkButtonAction(pydantic.BaseModel):
    type: typing.Optional["BaseLinkButtonActionType"] = pydantic.Field(
        None,
        description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="Action URL",
    )
    consume_reason: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class BaseLinkProduct(pydantic.BaseModel):
    price: "MarketPrice" = pydantic.Field(
        ...,
        description="",
    )
    merchant: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    orders_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class BaseLinkRating(pydantic.BaseModel):
    reviews_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Count of reviews",
    )
    stars: typing.Optional[int] = pydantic.Field(
        None,
        description="Count of stars",
    )


class BaseObjectCount(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Items count",
    )


class BasePlace(pydantic.BaseModel):
    address: typing.Optional[str] = pydantic.Field(
        None,
        description="Place address",
    )
    checkins: typing.Optional[int] = pydantic.Field(
        None,
        description="Checkins number",
    )
    city: typing.Optional[str] = pydantic.Field(
        None,
        description="City name",
    )
    country: typing.Optional[str] = pydantic.Field(
        None,
        description="Country name",
    )
    created: typing.Optional[int] = pydantic.Field(
        None,
        description="Date of the place creation in Unixtime",
    )
    icon: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the place's icon",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Place ID",
    )
    latitude: typing.Optional[int] = pydantic.Field(
        None,
        description="Place latitude",
    )
    longitude: typing.Optional[int] = pydantic.Field(
        None,
        description="Place longitude",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Place title",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Place type",
    )


class BaseRepostsInfo(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Total reposts counter. Sum of wall and mail reposts counters",
    )
    wall_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Wall reposts counter",
    )
    mail_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Mail reposts counter",
    )
    user_reposted: typing.Optional[int] = pydantic.Field(
        None,
        description="Information whether current user has reposted the post",
    )


class BaseSticker(pydantic.BaseModel):
    sticker_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Sticker ID",
    )
    product_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Pack ID",
    )
    images: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="",
    )
    images_with_background: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="",
    )
    animation_url: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of sticker animation script",
    )
    animations: typing.Optional[typing.List["BaseStickerAnimation"]] = pydantic.Field(
        None,
        description="Array of sticker animation script objects",
    )
    is_allowed: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the sticker is allowed",
    )


class BoardTopic(pydantic.BaseModel):
    comments: typing.Optional[int] = pydantic.Field(
        None,
        description="Comments number",
    )
    created: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the topic has been created in Unixtime",
    )
    created_by: typing.Optional[int] = pydantic.Field(
        None,
        description="Creator ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Topic ID",
    )
    is_closed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the topic is closed",
    )
    is_fixed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the topic is fixed",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Topic title",
    )
    updated: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the topic has been updated in Unixtime",
    )
    updated_by: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of user who updated the topic",
    )


class CommentThread(pydantic.BaseModel):
    can_post: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether current user can comment the post",
    )
    count: int = pydantic.Field(
        ...,
        description="Comments number",
    )
    groups_can_post: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether groups can comment the post",
    )
    items: typing.Optional[typing.List["WallWallComment"]] = pydantic.Field(
        None,
        description="",
    )
    show_reply_button: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether recommended to display reply button",
    )


class DocsDoc(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Document ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Document owner ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Document title",
    )
    size: int = pydantic.Field(
        ...,
        description="File size in bites",
    )
    ext: str = pydantic.Field(
        ...,
        description="File extension",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="File URL",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when file has been uploaded in Unixtime",
    )
    type: int = pydantic.Field(
        ...,
        description="Document type",
    )
    preview: typing.Optional["DocsDocPreview"] = pydantic.Field(
        None,
        description="",
    )
    is_licensed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the document",
    )
    tags: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="Document tags",
    )


class DocsDocPreview(pydantic.BaseModel):
    audio_msg: typing.Optional["DocsDocPreviewAudioMsg"] = pydantic.Field(
        None,
        description="",
    )
    graffiti: typing.Optional["DocsDocPreviewGraffiti"] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["DocsDocPreviewPhoto"] = pydantic.Field(
        None,
        description="",
    )
    video: typing.Optional["DocsDocPreviewVideo"] = pydantic.Field(
        None,
        description="",
    )


class DocsDocPreviewAudioMsg(pydantic.BaseModel):
    duration: int = pydantic.Field(
        ...,
        description="Audio message duration in seconds",
    )
    link_mp3: str = pydantic.Field(
        ...,
        description="MP3 file URL",
    )
    link_ogg: str = pydantic.Field(
        ...,
        description="OGG file URL",
    )
    waveform: typing.List[int] = pydantic.Field(
        ...,
        description="",
    )


class DocsDocPreviewGraffiti(pydantic.BaseModel):
    src: str = pydantic.Field(
        ...,
        description="Graffiti file URL",
    )
    width: int = pydantic.Field(
        ...,
        description="Graffiti width",
    )
    height: int = pydantic.Field(
        ...,
        description="Graffiti height",
    )


class DocsDocPreviewPhoto(pydantic.BaseModel):
    sizes: typing.Optional[typing.List["DocsDocPreviewPhotoSizes"]] = pydantic.Field(
        None,
        description="",
    )


class DocsDocPreviewVideo(pydantic.BaseModel):
    src: str = pydantic.Field(
        ...,
        description="Video URL",
    )
    width: int = pydantic.Field(
        ...,
        description="Video's width in pixels",
    )
    height: int = pydantic.Field(
        ...,
        description="Video's height in pixels",
    )
    file_size: int = pydantic.Field(
        ...,
        description="Video file size in bites",
    )


class EventsEventAttach(pydantic.BaseModel):
    address: typing.Optional[str] = pydantic.Field(
        None,
        description="address of event",
    )
    button_text: str = pydantic.Field(
        ...,
        description="text of attach",
    )
    friends: typing.List[int] = pydantic.Field(
        ...,
        description="array of friends ids",
    )
    id: int = pydantic.Field(
        ...,
        description="event ID",
    )
    is_favorite: bool = pydantic.Field(
        ...,
        description="is favorite",
    )
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = pydantic.Field(
        None,
        description="Current user's member status",
    )
    text: str = pydantic.Field(
        ...,
        description="text of attach",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="event start time",
    )


class FriendsRequestsMutual(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Total mutual friends number",
    )
    users: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )


class GiftsLayout(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Gift ID",
    )
    thumb_512: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 512 px in width",
    )
    thumb_256: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 256 px in width",
    )
    thumb_48: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 48 px in width",
    )
    thumb_96: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 96 px in width",
    )
    stickers_product_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the sticker pack, if the gift is representing one",
    )
    is_stickers_style: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether gift represents a stickers style",
    )
    build_id: typing.Optional[str] = pydantic.Field(
        None,
        description="ID of the build of constructor gift",
    )
    keywords: typing.Optional[str] = pydantic.Field(
        None,
        description="Keywords used for search",
    )


class GroupsAddressTimetable(pydantic.BaseModel):
    fri: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None,
        description="Timetable for friday",
    )
    mon: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None,
        description="Timetable for monday",
    )
    sat: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None,
        description="Timetable for saturday",
    )
    sun: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None,
        description="Timetable for sunday",
    )
    thu: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None,
        description="Timetable for thursday",
    )
    tue: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None,
        description="Timetable for tuesday",
    )
    wed: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None,
        description="Timetable for wednesday",
    )


class GroupsAddressTimetableDay(pydantic.BaseModel):
    break_close_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Close time of the break in minutes",
    )
    break_open_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Start time of the break in minutes",
    )
    close_time: int = pydantic.Field(
        ...,
        description="Close time in minutes",
    )
    open_time: int = pydantic.Field(
        ...,
        description="Open time in minutes",
    )


class GroupsBanInfo(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Administrator ID",
    )
    comment: typing.Optional[str] = pydantic.Field(
        None,
        description="Comment for a ban",
    )
    comment_visible: typing.Optional[bool] = pydantic.Field(
        None,
        description="Show comment for user",
    )
    is_closed: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when user has been added to blacklist in Unixtime",
    )
    end_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when user will be removed from blacklist in Unixtime",
    )
    reason: typing.Optional["GroupsBanInfoReason"] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroup(pydantic.BaseModel):
    admin_level: typing.Optional["GroupsGroupAdminLevel"] = pydantic.Field(
        None,
        description="",
    )
    deactivated: typing.Optional[str] = pydantic.Field(
        None,
        description="Information whether community is banned",
    )
    finish_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Finish date in Unixtime format",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Community ID",
    )
    is_admin: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is administrator",
    )
    is_advertiser: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is advertiser",
    )
    is_closed: typing.Optional["GroupsGroupIsClosed"] = pydantic.Field(
        None,
        description="",
    )
    is_member: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is member",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Community name",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 100 pixels in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 200 pixels in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 50 pixels in width",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Domain of the community page",
    )
    start_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Start date in Unixtime format",
    )
    type: typing.Optional["GroupsGroupType"] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupAttach(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="group ID",
    )
    text: str = pydantic.Field(
        ...,
        description="text of attach",
    )
    status: str = pydantic.Field(
        ...,
        description="activity or category of group",
    )
    size: int = pydantic.Field(
        ...,
        description="size of group",
    )
    is_favorite: bool = pydantic.Field(
        ...,
        description="is favorite",
    )


class GroupsLongPollEvents(pydantic.BaseModel):
    audio_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    board_post_delete: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    board_post_edit: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    board_post_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    board_post_restore: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    group_change_photo: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    group_change_settings: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    group_join: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    group_leave: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    group_officers_edit: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    lead_forms_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    market_comment_delete: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    market_comment_edit: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    market_comment_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    market_comment_restore: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    market_order_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    market_order_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    message_allow: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    message_deny: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    message_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    message_read: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    message_reply: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    message_typing_state: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    message_edit: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    photo_comment_delete: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    photo_comment_edit: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    photo_comment_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    photo_comment_restore: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    photo_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    poll_vote_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    user_block: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    user_unblock: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    video_comment_delete: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    video_comment_edit: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    video_comment_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    video_comment_restore: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    video_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    wall_post_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    wall_reply_delete: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    wall_reply_edit: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    wall_reply_new: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    wall_reply_restore: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )
    wall_repost: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )


class LinkTargetObject(pydantic.BaseModel):
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Object type",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Owner ID",
    )
    item_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Item ID",
    )


class MarketCurrency(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Currency ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Currency sign",
    )


class MarketMarketAlbum(pydantic.BaseModel):
    count: int = pydantic.Field(
        ...,
        description="Items number",
    )
    id: int = pydantic.Field(
        ...,
        description="Market album ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Market album owner's ID",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    title: str = pydantic.Field(
        ...,
        description="Market album title",
    )
    updated_time: int = pydantic.Field(
        ...,
        description="Date when album has been updated last time in Unixtime",
    )


class MarketMarketCategory(pydantic.BaseModel):
    pass


class MarketMarketCategoryNested(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Category ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Category name",
    )
    parent: typing.Optional["MarketMarketCategoryNested"] = pydantic.Field(
        None,
        description="",
    )


class MarketMarketItem(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the market item",
    )
    availability: "MarketMarketItemAvailability" = pydantic.Field(
        ...,
        description="",
    )
    button_title: typing.Optional[str] = pydantic.Field(
        None,
        description="Title for button for url",
    )
    category: "MarketMarketCategory" = pydantic.Field(
        ...,
        description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the item has been created in Unixtime",
    )
    description: str = pydantic.Field(
        ...,
        description="Item description",
    )
    external_id: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="Item ID",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Item owner's ID",
    )
    price: "MarketPrice" = pydantic.Field(
        ...,
        description="",
    )
    thumb_photo: str = pydantic.Field(
        ...,
        description="URL of the preview image",
    )
    title: str = pydantic.Field(
        ...,
        description="Item title",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="URL to item",
    )
    variants_grouping_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    is_main_variant: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    sku: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class MarketPrice(pydantic.BaseModel):
    amount: typing.Optional[str] = pydantic.Field(
        None,
        description="Amount",
    )
    currency: typing.Optional["MarketCurrency"] = pydantic.Field(
        None,
        description="",
    )
    discount_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    old_amount: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Text",
    )
    old_amount_text: typing.Optional[str] = pydantic.Field(
        None,
        description="Textual representation of old price",
    )


class MarketSection(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Section ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Section name",
    )


class MediaRestriction(pydantic.BaseModel):
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    title: str = pydantic.Field(
        ...,
        description="",
    )
    button: typing.Optional["VideoRestrictionButton"] = pydantic.Field(
        None,
        description="",
    )
    always_shown: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Need show restriction always or not",
    )
    blur: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Need blur current video or not",
    )
    can_play: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Can play video or not",
    )
    can_preview: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Can preview video or not",
    )
    card_icon: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="",
    )
    list_icon: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="",
    )


class MessagesAudioMessage(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for audio message",
    )
    transcript_error: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    transcript: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    duration: int = pydantic.Field(
        ...,
        description="Audio message duration in seconds",
    )
    id: int = pydantic.Field(
        ...,
        description="Audio message ID",
    )
    link_mp3: str = pydantic.Field(
        ...,
        description="MP3 file URL",
    )
    link_ogg: str = pydantic.Field(
        ...,
        description="OGG file URL",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Audio message owner ID",
    )
    waveform: typing.List[int] = pydantic.Field(
        ...,
        description="",
    )


class MessagesChatPushSettings(pydantic.BaseModel):
    disabled_until: typing.Optional[int] = pydantic.Field(
        None,
        description="Time until that notifications are disabled",
    )
    sound: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the sound is on",
    )


class MessagesConversation(pydantic.BaseModel):
    peer: "MessagesConversationPeer" = pydantic.Field(
        ...,
        description="",
    )
    last_message_id: int = pydantic.Field(
        ...,
        description="ID of the last message in conversation",
    )
    in_read: int = pydantic.Field(
        ...,
        description="Last message user have read",
    )
    out_read: int = pydantic.Field(
        ...,
        description="Last outcoming message have been read by the opponent",
    )
    unread_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Unread messages number",
    )
    is_marked_unread: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is this conversation uread",
    )
    out_read_by: typing.Optional["MessagesOutReadBy"] = pydantic.Field(
        None,
        description="",
    )
    important: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    unanswered: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    special_service_type: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    message_request_data: typing.Optional["MessagesMessageRequestData"] = pydantic.Field(
        None,
        description="",
    )
    mentions: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="Ids of messages with mentions",
    )
    current_keyboard: typing.Optional["MessagesKeyboard"] = pydantic.Field(
        None,
        description="",
    )

    can_write: typing.Optional["MessagesConversationCanWrite"] = pydantic.Field(
        None,
        description="Information about whether you can write to the dialog",
    )  # extension_field
    chat_settings: typing.Optional["MessagesConversationChatSettings"] = pydantic.Field(
        None,
        description="Chat settings",
    )  # extension_field


class MessagesConversationCanWrite(pydantic.BaseModel):  # extension_class
    allowed: typing.Optional[bool] = pydantic.Field(
        None,
        description="Can the user write to the dialog",
    )
    reason: typing.Optional[int] = pydantic.Field(
        None,
        description="Reason code why the user can't write to the dialog",
    )


class MessagesConversationChatSettings(pydantic.BaseModel):  # extension_class
    members_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of chat members",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Chat title",
    )
    pinned_message: typing.Optional["MessagesPinnedMessage"] = pydantic.Field(
        None,
        description="Pinned message object",
    )
    state: typing.Optional[str] = pydantic.Field(
        None,
        description="Status of the current user in the chat",
    )
    photo: typing.Optional["MessagesMessageActionPhoto"] = pydantic.Field(
        None,
        description="The cover image of the chat",
    )
    active_ids: typing.Optional[list] = pydantic.Field(
        None,
        description="IDs of the last users who wrote to the chat",
    )
    is_group_channel: typing.Optional[bool] = pydantic.Field(
        None,
        description="information about whether the conversation is a community channel",
    )


class MessagesConversationPeer(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    local_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    type: "MessagesConversationPeerType" = pydantic.Field(
        ...,
        description="",
    )


class MessagesForeignMessage(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Conversation message ID",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the message was created",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Message author's ID",
    )
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = pydantic.Field(
        None,
        description="",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None,
        description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Message ID",
    )
    peer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Peer ID",
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = pydantic.Field(
        None,
        description="",
    )
    text: str = pydantic.Field(
        ...,
        description="Message text",
    )
    update_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the message has been updated in Unixtime",
    )
    was_listened: typing.Optional[bool] = pydantic.Field(
        None,
        description="Was the audio message inside already listened by you",
    )
    payload: typing.Optional[str] = pydantic.Field(
        None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesGraffiti(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for graffiti",
    )
    height: int = pydantic.Field(
        ...,
        description="Graffiti height",
    )
    id: int = pydantic.Field(
        ...,
        description="Graffiti ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Graffiti owner ID",
    )
    url: str = pydantic.Field(
        ...,
        description="Graffiti URL",
    )
    width: int = pydantic.Field(
        ...,
        description="Graffiti width",
    )


class MessagesHistoryMessageAttachment(pydantic.BaseModel):
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    audio_message: typing.Optional["MessagesAudioMessage"] = pydantic.Field(
        None,
        description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None,
        description="",
    )
    graffiti: typing.Optional["MessagesGraffiti"] = pydantic.Field(
        None,
        description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    market: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    share: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    type: "MessagesHistoryMessageAttachmentType" = pydantic.Field(
        ...,
        description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="",
    )
    wall: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )


class MessagesKeyboard(pydantic.BaseModel):
    author_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Community or bot, which set this keyboard",
    )
    buttons: typing.List[typing.List["MessagesKeyboardButton"]] = pydantic.Field(
        ...,
        description="",
    )
    one_time: bool = pydantic.Field(
        ...,
        description="Should this keyboard disappear on first use",
    )
    inline: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )


class MessagesKeyboardButtonAction(pydantic.BaseModel):
    app_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Fragment value in app link like vk.com/app{app_id}_-654321#hash",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Fragment value in app link like vk.com/app123456_-654321#{hash}",
    )
    label: typing.Optional[str] = pydantic.Field(
        None,
        description="Label for button",
    )
    link: typing.Optional[str] = pydantic.Field(
        None,
        description="link for button",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Fragment value in app link like vk.com/app123456_{owner_id}#hash",
    )
    payload: typing.Optional[str] = pydantic.Field(
        None,
        description="Additional data sent along with message for developer convenience",
    )
    type: "MessagesTemplateActionTypeNames" = pydantic.Field(
        ...,
        description="Button type",
    )


class MessagesMessage(pydantic.BaseModel):
    action: typing.Optional["MessagesMessageAction"] = pydantic.Field(
        None,
        description="",
    )
    admin_author_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Only for messages from community. Contains user ID of community admin, who sent this message.",
    )
    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Unique auto-incremented number for all messages with this peer",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the message has been sent in Unixtime",
    )
    deleted: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Is it an deleted message",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Message author's ID",
    )
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = pydantic.Field(
        None,
        description="Forwarded messages",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="Message ID",
    )
    important: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is it an important message",
    )
    is_hidden: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    is_cropped: typing.Optional[bool] = pydantic.Field(
        None,
        description="this message is cropped for bot",
    )
    keyboard: typing.Optional["MessagesKeyboard"] = pydantic.Field(
        None,
        description="",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Members number",
    )
    out: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether the message is outcoming",
    )
    payload: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    peer_id: int = pydantic.Field(
        ...,
        description="Peer ID",
    )
    random_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID used for sending messages. It returned only for outgoing messages",
    )
    ref: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    ref_source: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = pydantic.Field(
        None,
        description="",
    )
    text: str = pydantic.Field(
        ...,
        description="Message text",
    )
    update_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the message has been updated in Unixtime",
    )
    was_listened: typing.Optional[bool] = pydantic.Field(
        None,
        description="Was the audio message inside already listened by you",
    )
    pinned_at: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the message has been pinned in Unixtime",
    )


class MessagesMessageAction(pydantic.BaseModel):
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Message ID",
    )
    email: typing.Optional[str] = pydantic.Field(
        None,
        description="Email address for chat_invite_user or chat_kick_user actions",
    )
    member_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User or email peer ID",
    )
    message: typing.Optional[str] = pydantic.Field(
        None,
        description="Message body of related message",
    )
    photo: typing.Optional["MessagesMessageActionPhoto"] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="New chat title for chat_create and chat_title_update actions",
    )
    type: "MessagesMessageActionStatus" = pydantic.Field(
        ...,
        description="",
    )


class MessagesMessageActionPhoto(pydantic.BaseModel):
    photo_100: str = pydantic.Field(
        ...,
        description="URL of the preview image with 100px in width",
    )
    photo_200: str = pydantic.Field(
        ...,
        description="URL of the preview image with 200px in width",
    )
    photo_50: str = pydantic.Field(
        ...,
        description="URL of the preview image with 50px in width",
    )


class MessagesMessageRequestData(pydantic.BaseModel):
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Status of message request",
    )
    inviter_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Message request sender id",
    )
    request_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Message request date",
    )


class MessagesOutReadBy(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    member_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemDigestFooterButton(pydantic.BaseModel):
    title: str = pydantic.Field(
        ...,
        description="",
    )
    style: str = pydantic.Field(
        ...,
        description="",
    )


class NotificationsFeedback(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Reply author's ID",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None,
        description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Item ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Reply text",
    )
    to_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Wall owner's ID",
    )


class NotificationsReply(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the reply has been created in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Reply ID",
    )
    text: typing.Optional[int] = pydantic.Field(
        None,
        description="Reply text",
    )


class NotificationsSendMessageError(pydantic.BaseModel):
    code: typing.Optional[int] = pydantic.Field(
        None,
        description="Error code",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Error description",
    )


class PagesWikipageFull(pydantic.BaseModel):
    created: int = pydantic.Field(
        ...,
        description="Date when the page has been created in Unixtime",
    )
    creator_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Page creator ID",
    )
    current_user_can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can edit the page",
    )
    current_user_can_edit_access: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can edit the page access settings",
    )
    edited: int = pydantic.Field(
        ...,
        description="Date when the page has been edited in Unixtime",
    )
    editor_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Last editor ID",
    )
    group_id: int = pydantic.Field(
        ...,
        description="Community ID",
    )
    html: typing.Optional[str] = pydantic.Field(
        None,
        description="Page content, HTML",
    )
    id: int = pydantic.Field(
        ...,
        description="Page ID",
    )
    source: typing.Optional[str] = pydantic.Field(
        None,
        description="Page content, wiki",
    )
    title: str = pydantic.Field(
        ...,
        description="Page title",
    )
    view_url: str = pydantic.Field(
        ...,
        description="URL of the page preview",
    )
    views: int = pydantic.Field(
        ...,
        description="Views number",
    )
    who_can_edit: "PagesPrivacySettings" = pydantic.Field(
        ...,
        description="Edit settings of the page",
    )
    who_can_view: "PagesPrivacySettings" = pydantic.Field(
        ...,
        description="View settings of the page",
    )


class PhotosPhoto(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the photo",
    )
    album_id: int = pydantic.Field(
        ...,
        description="Album ID",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo height",
    )
    id: int = pydantic.Field(
        ...,
        description="Photo ID",
    )
    images: typing.Optional[typing.List["PhotosImage"]] = pydantic.Field(
        None,
        description="",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None,
        description="Latitude",
    )
    long: typing.Optional[int] = pydantic.Field(
        None,
        description="Longitude",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Photo owner's ID",
    )
    photo_256: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 2560 px width",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the photo",
    )
    place: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo width",
    )
    has_tags: bool = pydantic.Field(
        ...,
        description="Whether photo has attached tag links",
    )
    restrictions: typing.Optional["MediaRestriction"] = pydantic.Field(
        None,
        description="",
    )


class PhotosPhotoAlbum(pydantic.BaseModel):
    created: int = pydantic.Field(
        ...,
        description="Date when the album has been created in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo album description",
    )
    id: int = pydantic.Field(
        ...,
        description="Photo album ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Album owner's ID",
    )
    size: int = pydantic.Field(
        ...,
        description="Photos number",
    )
    thumb: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    title: str = pydantic.Field(
        ...,
        description="Photo album title",
    )
    updated: int = pydantic.Field(
        ...,
        description="Date when the album has been updated last time in Unixtime",
    )


class PollsBackground(pydantic.BaseModel):
    angle: typing.Optional[int] = pydantic.Field(
        None,
        description="Gradient angle with 0 on positive X axis",
    )
    color: typing.Optional[str] = pydantic.Field(
        None,
        description="Hex color code without #",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Original height of pattern tile",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    images: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="Pattern tiles",
    )
    points: typing.Optional[typing.List["BaseGradientPoint"]] = pydantic.Field(
        None,
        description="Gradient points",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Original with of pattern tile",
    )


class PollsPoll(pydantic.BaseModel):
    anonymous: bool = pydantic.Field(
        ...,
        description="",
    )
    friends: typing.Optional[typing.List["PollsFriend"]] = pydantic.Field(
        None,
        description="",
    )
    multiple: bool = pydantic.Field(
        ...,
        description="Information whether the poll with multiple choices",
    )
    answer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Current user's answer ID",
    )
    end_date: int = pydantic.Field(
        ...,
        description="",
    )
    answer_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="Current user's answer IDs",
    )
    closed: bool = pydantic.Field(
        ...,
        description="",
    )
    is_board: bool = pydantic.Field(
        ...,
        description="",
    )
    can_edit: bool = pydantic.Field(
        ...,
        description="",
    )
    can_vote: bool = pydantic.Field(
        ...,
        description="",
    )
    can_report: bool = pydantic.Field(
        ...,
        description="",
    )
    can_share: bool = pydantic.Field(
        ...,
        description="",
    )
    photo: typing.Optional["PollsBackground"] = pydantic.Field(
        None,
        description="",
    )
    answers: typing.List["PollsAnswer"] = pydantic.Field(
        ...,
        description="",
    )
    created: int = pydantic.Field(
        ...,
        description="Date when poll has been created in Unixtime",
    )
    id: int = pydantic.Field(
        ...,
        description="Poll ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Poll owner's ID",
    )
    author_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Poll author's ID",
    )
    question: str = pydantic.Field(
        ...,
        description="Poll question",
    )
    background: typing.Optional["PollsBackground"] = pydantic.Field(
        None,
        description="",
    )
    votes: int = pydantic.Field(
        ...,
        description="Votes number",
    )
    disable_unvote: bool = pydantic.Field(
        ...,
        description="",
    )


class PollsVotersUsers(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Votes number",
    )
    items: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )


class StatsActivity(pydantic.BaseModel):
    comments: typing.Optional[int] = pydantic.Field(
        None,
        description="Comments number",
    )
    copies: typing.Optional[int] = pydantic.Field(
        None,
        description="Reposts number",
    )
    hidden: typing.Optional[int] = pydantic.Field(
        None,
        description="Hidden from news count",
    )
    likes: typing.Optional[int] = pydantic.Field(
        None,
        description="Likes number",
    )
    subscribed: typing.Optional[int] = pydantic.Field(
        None,
        description="New subscribers count",
    )
    unsubscribed: typing.Optional[int] = pydantic.Field(
        None,
        description="Unsubscribed count",
    )


class StatsReach(pydantic.BaseModel):
    age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )
    cities: typing.Optional[typing.List["StatsCity"]] = pydantic.Field(
        None,
        description="",
    )
    countries: typing.Optional[typing.List["StatsCountry"]] = pydantic.Field(
        None,
        description="",
    )
    mobile_reach: typing.Optional[int] = pydantic.Field(
        None,
        description="Reach count from mobile devices",
    )
    reach: typing.Optional[int] = pydantic.Field(
        None,
        description="Reach count",
    )
    reach_subscribers: typing.Optional[int] = pydantic.Field(
        None,
        description="Subscribers reach count",
    )
    sex: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )


class StatsViews(pydantic.BaseModel):
    age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )
    cities: typing.Optional[typing.List["StatsCity"]] = pydantic.Field(
        None,
        description="",
    )
    countries: typing.Optional[typing.List["StatsCountry"]] = pydantic.Field(
        None,
        description="",
    )
    mobile_views: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of views from mobile devices",
    )
    sex: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Views number",
    )
    visitors: typing.Optional[int] = pydantic.Field(
        None,
        description="Visitors number",
    )


class StoriesClickableStickers(pydantic.BaseModel):
    clickable_stickers: typing.List["StoriesClickableSticker"] = pydantic.Field(
        ...,
        description="",
    )
    original_height: int = pydantic.Field(
        ...,
        description="",
    )
    original_width: int = pydantic.Field(
        ...,
        description="",
    )


class StoriesPromoBlock(pydantic.BaseModel):
    name: str = pydantic.Field(
        ...,
        description="Promo story title",
    )
    photo_50: str = pydantic.Field(
        ...,
        description="RL of square photo of the story with 50 pixels in width",
    )
    photo_100: str = pydantic.Field(
        ...,
        description="RL of square photo of the story with 100 pixels in width",
    )
    not_animated: bool = pydantic.Field(
        ...,
        description="Hide animation for promo story",
    )


class StoriesReplies(pydantic.BaseModel):
    count: int = pydantic.Field(
        ...,
        description="Replies number.",
    )
    new: typing.Optional[int] = pydantic.Field(
        None,
        description="New replies number.",
    )


class StoriesStory(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for private object.",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the story (0 - no, 1 - yes).",
    )
    can_reply: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can reply to the story (0 - no, 1 - yes).",
    )
    can_see: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see the story (0 - no, 1 - yes).",
    )
    can_like: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether current user can like the story.",
    )
    can_share: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can share the story (0 - no, 1 - yes).",
    )
    can_hide: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can hide the story (0 - no, 1 - yes).",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when story has been added in Unixtime.",
    )
    expires_at: typing.Optional[int] = pydantic.Field(
        None,
        description="Story expiration time. Unixtime.",
    )
    id: int = pydantic.Field(
        ...,
        description="Story ID.",
    )
    is_deleted: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the story is deleted (false - no, true - yes).",
    )
    is_expired: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the story is expired (false - no, true - yes).",
    )
    link: typing.Optional["StoriesStoryLink"] = pydantic.Field(
        None,
        description="",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Story owner's ID.",
    )
    parent_story: typing.Optional["StoriesStory"] = pydantic.Field(
        None,
        description="",
    )
    parent_story_access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for private object.",
    )
    parent_story_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Parent story ID.",
    )
    parent_story_owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Parent story owner's ID.",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    replies: typing.Optional["StoriesReplies"] = pydantic.Field(
        None,
        description="Replies counters to current story.",
    )
    seen: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user has seen the story or not (0 - no, 1 - yes).",
    )
    type: typing.Optional["StoriesStoryType"] = pydantic.Field(
        None,
        description="",
    )
    clickable_stickers: typing.Optional["StoriesClickableStickers"] = pydantic.Field(
        None,
        description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Views number.",
    )
    can_ask: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether story has question sticker and current user can send question to the author",
    )
    can_ask_anonymous: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether story has question sticker and current user can send anonymous question to the author",
    )
    narratives_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    first_narrative_title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    birthday_wish_user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    can_use_in_narrative: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )


class StoriesStoryLink(pydantic.BaseModel):
    text: str = pydantic.Field(
        ...,
        description="Link text",
    )
    url: str = pydantic.Field(
        ...,
        description="Link URL",
    )


class StoriesStoryStatsStat(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Stat value",
    )
    state: "StoriesStoryStatsState" = pydantic.Field(
        ...,
        description="",
    )


class UsersPersonal(pydantic.BaseModel):
    alcohol: typing.Optional[int] = pydantic.Field(
        None,
        description="User's views on alcohol",
    )
    inspired_by: typing.Optional[str] = pydantic.Field(
        None,
        description="User's inspired by",
    )
    langs: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="",
    )
    life_main: typing.Optional[int] = pydantic.Field(
        None,
        description="User's personal priority in life",
    )
    people_main: typing.Optional[int] = pydantic.Field(
        None,
        description="User's personal priority in people",
    )
    political: typing.Optional[int] = pydantic.Field(
        None,
        description="User's political views",
    )
    religion: typing.Optional[str] = pydantic.Field(
        None,
        description="User's religion",
    )
    religion_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User's religion id",
    )
    smoking: typing.Optional[int] = pydantic.Field(
        None,
        description="User's views on smoking",
    )


class UsersUserConnections(pydantic.BaseModel):
    skype: str = pydantic.Field(
        ...,
        description="User's Skype nickname",
    )
    facebook: str = pydantic.Field(
        ...,
        description="User's Facebook account",
    )
    facebook_name: typing.Optional[str] = pydantic.Field(
        None,
        description="User's Facebook name",
    )
    twitter: str = pydantic.Field(
        ...,
        description="User's Twitter account",
    )
    livejournal: typing.Optional[str] = pydantic.Field(
        None,
        description="User's Livejournal account",
    )
    instagram: str = pydantic.Field(
        ...,
        description="User's Instagram account",
    )


class UsersUserMin(pydantic.BaseModel):
    deactivated: typing.Optional[str] = pydantic.Field(
        None,
        description="Returns if a profile is deleted or blocked",
    )
    first_name: typing.Optional[str] = pydantic.Field(
        None,
        description="User first name",
    )
    hidden: typing.Optional[int] = pydantic.Field(
        None,
        description="Returns if a profile is hidden.",
    )
    id: int = pydantic.Field(
        ...,
        description="User ID",
    )
    last_name: typing.Optional[str] = pydantic.Field(
        None,
        description="User last name",
    )
    can_access_closed: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    is_closed: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )


class VideoRestrictionButton(pydantic.BaseModel):
    action: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class WallAppPost(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Application ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Application name",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 130 px in width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 604 px in width",
    )


class WallAttachedNote(pydantic.BaseModel):
    comments: int = pydantic.Field(
        ...,
        description="Comments number",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the note has been created in Unixtime",
    )
    id: int = pydantic.Field(
        ...,
        description="Note ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Note owner's ID",
    )
    read_comments: int = pydantic.Field(
        ...,
        description="Read comments number",
    )
    title: str = pydantic.Field(
        ...,
        description="Note title",
    )
    view_url: str = pydantic.Field(
        ...,
        description="URL of the page with note preview",
    )


class WallGeo(pydantic.BaseModel):
    coordinates: typing.Optional[str] = pydantic.Field(
        None,
        description="Coordinates as string. <latitude> <longtitude>",
    )
    place: typing.Optional["BasePlace"] = pydantic.Field(
        None,
        description="",
    )
    showmap: typing.Optional[int] = pydantic.Field(
        None,
        description="Information whether a map is showed",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Place type",
    )


class WallGraffiti(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Graffiti ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Graffiti owner's ID",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 200 px in width",
    )
    photo_586: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 586 px in width",
    )


class WallPostCopyright(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    link: str = pydantic.Field(
        ...,
        description="",
    )
    name: str = pydantic.Field(
        ...,
        description="",
    )
    type: str = pydantic.Field(
        ...,
        description="",
    )


class WallPostSource(pydantic.BaseModel):
    data: typing.Optional[str] = pydantic.Field(
        None,
        description="Additional data",
    )
    platform: typing.Optional[str] = pydantic.Field(
        None,
        description="Platform name",
    )
    type: typing.Optional["WallPostSourceType"] = pydantic.Field(
        None,
        description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="URL to an external site used to publish the post",
    )


class WallPostedPhoto(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Photo ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Photo owner's ID",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 130 px in width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 604 px in width",
    )


class WallViews(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Count",
    )


class WallWallComment(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the comment has been added in Unixtime",
    )
    donut: typing.Optional["WallWallCommentDonut"] = pydantic.Field(
        None,
        description="",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Author ID",
    )
    id: int = pydantic.Field(
        ...,
        description="Comment ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None,
        description="Real position of the comment",
    )
    reply_to_comment: typing.Optional[int] = pydantic.Field(
        None,
        description="Replied comment ID",
    )
    reply_to_user: typing.Optional[int] = pydantic.Field(
        None,
        description="Replied user ID",
    )
    text: str = pydantic.Field(
        ...,
        description="Comment text",
    )
    thread: typing.Optional["CommentThread"] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    parents_stack: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    deleted: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )


class WallWallCommentDonut(pydantic.BaseModel):
    is_don: typing.Optional[bool] = pydantic.Field(
        None,
        description="Means commentator is donator",
    )
    placeholder: typing.Optional["WallWallCommentDonutPlaceholder"] = pydantic.Field(
        None,
        description="",
    )


class WallWallCommentDonutPlaceholder(pydantic.BaseModel):
    text: str = pydantic.Field(
        ...,
        description="",
    )


class WallWallpost(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key to private object",
    )
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    copyright: typing.Optional["WallPostCopyright"] = pydantic.Field(
        None,
        description="Information about the source of the post",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date of publishing in Unixtime",
    )
    edited: typing.Optional[int] = pydantic.Field(
        None,
        description="Date of editing in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post author ID",
    )
    geo: typing.Optional["WallGeo"] = pydantic.Field(
        None,
        description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    is_archived: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is post archived, only for post owners",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the post in favorites list",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="Count of likes",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Wall owner's ID",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None,
        description="",
    )
    post_type: typing.Optional["WallPostType"] = pydantic.Field(
        None,
        description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None,
        description="",
    )
    signer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post signer ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Post text",
    )
    views: typing.Optional["WallViews"] = pydantic.Field(
        None,
        description="Count of views",
    )


class WallWallpostCommentsDonut(pydantic.BaseModel):
    placeholder: typing.Optional["WallWallpostCommentsDonutPlaceholder"] = pydantic.Field(
        None,
        description="",
    )


class WallWallpostCommentsDonutPlaceholder(pydantic.BaseModel):
    text: str = pydantic.Field(
        ...,
        description="",
    )


class WallWallpostDonutPlaceholder(pydantic.BaseModel):
    text: str = pydantic.Field(
        ...,
        description="",
    )


class WidgetsCommentMedia(pydantic.BaseModel):
    item_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Media item ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Media owner's ID",
    )
    thumb_src: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image (type=photo only)",
    )
    type: typing.Optional["WidgetsCommentMediaType"] = pydantic.Field(
        None,
        description="",
    )


class WidgetsCommentReplies(pydantic.BaseModel):
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the post",
    )
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Comments number",
    )
    replies: typing.Optional[typing.List["WidgetsCommentRepliesItem"]] = pydantic.Field(
        None,
        description="",
    )


class WidgetsWidgetLikes(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Likes number",
    )


class AccountAccountCounters(pydantic.BaseModel):
    app_requests: typing.Optional[int] = pydantic.Field(
        None,
        description="New app requests number",
    )
    events: typing.Optional[int] = pydantic.Field(
        None,
        description="New events number",
    )
    faves: typing.Optional[int] = pydantic.Field(
        None,
        description="New faves number",
    )
    friends: typing.Optional[int] = pydantic.Field(
        None,
        description="New friends requests number",
    )
    friends_suggestions: typing.Optional[int] = pydantic.Field(
        None,
        description="New friends suggestions number",
    )
    friends_recommendations: typing.Optional[int] = pydantic.Field(
        None,
        description="New friends recommendations number",
    )
    gifts: typing.Optional[int] = pydantic.Field(
        None,
        description="New gifts number",
    )
    groups: typing.Optional[int] = pydantic.Field(
        None,
        description="New groups number",
    )
    menu_discover_badge: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    menu_clips_badge: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    messages: typing.Optional[int] = pydantic.Field(
        None,
        description="New messages number",
    )
    memories: typing.Optional[int] = pydantic.Field(
        None,
        description="New memories number",
    )
    notes: typing.Optional[int] = pydantic.Field(
        None,
        description="New notes number",
    )
    notifications: typing.Optional[int] = pydantic.Field(
        None,
        description="New notifications number",
    )
    photos: typing.Optional[int] = pydantic.Field(
        None,
        description="New photo tags number",
    )
    sdk: typing.Optional[int] = pydantic.Field(
        None,
        description="New sdk number",
    )


class AccountInfo(pydantic.BaseModel):
    wishlists_ae_promo_banner_show: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    twofa_required: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Two factor authentication is enabled", alias="2fa_required"
    )
    country: typing.Optional[str] = pydantic.Field(
        None,
        description="Country code",
    )
    https_required: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether HTTPS-only is enabled",
    )
    intro: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether user has been processed intro",
    )
    show_vk_apps_intro: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    mini_apps_ads_slot_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Ads slot id for MyTarget",
    )
    qr_promotion: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    link_redirects: typing.Optional[dict] = pydantic.Field(
        None,
        description="",
    )
    lang: typing.Optional[int] = pydantic.Field(
        None,
        description="Language ID",
    )
    no_wall_replies: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether wall comments should be hidden",
    )
    own_posts_default: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether only owners posts should be shown",
    )
    subscriptions: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )


class AccountOffer(pydantic.BaseModel):
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Offer description",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Offer ID",
    )
    img: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image",
    )
    instruction: typing.Optional[str] = pydantic.Field(
        None,
        description="Instruction how to process the offer",
    )
    instruction_html: typing.Optional[str] = pydantic.Field(
        None,
        description="Instruction how to process the offer (HTML format)",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Offer price",
    )
    short_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Offer short description",
    )
    tag: typing.Optional[str] = pydantic.Field(
        None,
        description="Offer tag",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Offer title",
    )
    currency_amount: typing.Optional[int] = pydantic.Field(
        None,
        description="Currency amount",
    )
    link_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Link id",
    )
    link_type: typing.Optional[str] = pydantic.Field(
        None,
        description="Link type",
    )


class AccountPushConversationsItem(pydantic.BaseModel):
    disabled_until: int = pydantic.Field(
        ...,
        description="Time until that notifications are disabled in seconds",
    )
    peer_id: int = pydantic.Field(
        ...,
        description="Peer ID",
    )
    sound: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether the sound are enabled",
    )


class AccountPushSettings(pydantic.BaseModel):
    disabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether notifications are disabled",
    )
    disabled_until: typing.Optional[int] = pydantic.Field(
        None,
        description="Time until that notifications are disabled in Unixtime",
    )
    settings: typing.Optional["AccountPushParams"] = pydantic.Field(
        None,
        description="",
    )
    conversations: typing.Optional["AccountPushConversations"] = pydantic.Field(
        None,
        description="",
    )


class AdsAccesses(pydantic.BaseModel):
    client_id: typing.Optional[str] = pydantic.Field(
        None,
        description="Client ID",
    )
    role: typing.Optional["AdsAccessRole"] = pydantic.Field(
        None,
        description="",
    )


class AdsAccount(pydantic.BaseModel):
    access_role: "AdsAccessRole" = pydantic.Field(
        ...,
        description="",
    )
    account_id: int = pydantic.Field(
        ...,
        description="Account ID",
    )
    account_status: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether account is active",
    )
    account_type: "AdsAccountType" = pydantic.Field(
        ...,
        description="",
    )
    account_name: str = pydantic.Field(
        ...,
        description="Account name",
    )
    can_view_budget: bool = pydantic.Field(
        ...,
        description="Can user view account budget",
    )


class AdsAd(pydantic.BaseModel):
    ad_format: int = pydantic.Field(
        ...,
        description="Ad format",
    )
    ad_platform: typing.Optional[typing.Union[int, str,]] = pydantic.Field(
        None,
        description="Ad platform",
    )
    all_limit: int = pydantic.Field(
        ...,
        description="Total limit",
    )
    approved: "AdsAdApproved" = pydantic.Field(
        ...,
        description="",
    )
    campaign_id: int = pydantic.Field(
        ...,
        description="Campaign ID",
    )
    category1_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Category ID",
    )
    category2_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Additional category ID",
    )
    cost_type: "AdsAdCostType" = pydantic.Field(
        ...,
        description="",
    )
    cpc: typing.Optional[int] = pydantic.Field(
        None,
        description="Cost of a click, kopecks",
    )
    cpm: typing.Optional[int] = pydantic.Field(
        None,
        description="Cost of 1000 impressions, kopecks",
    )
    cpa: typing.Optional[int] = pydantic.Field(
        None,
        description="Cost of an action, kopecks",
    )
    ocpm: typing.Optional[int] = pydantic.Field(
        None,
        description="Cost of 1000 impressions optimized, kopecks",
    )
    autobidding_max_cost: typing.Optional[int] = pydantic.Field(
        None,
        description="Max cost of target actions for autobidding, kopecks",
    )
    disclaimer_medical: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether disclaimer is enabled",
    )
    disclaimer_specialist: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether disclaimer is enabled",
    )
    disclaimer_supplements: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether disclaimer is enabled",
    )
    id: int = pydantic.Field(
        ...,
        description="Ad ID",
    )
    impressions_limit: typing.Optional[int] = pydantic.Field(
        None,
        description="Impressions limit",
    )
    impressions_limited: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether impressions are limited",
    )
    name: str = pydantic.Field(
        ...,
        description="Ad title",
    )
    status: "AdsAdStatus" = pydantic.Field(
        ...,
        description="",
    )
    video: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the ad is a video",
    )


class AdsAdLayout(pydantic.BaseModel):
    ad_format: int = pydantic.Field(
        ...,
        description="Ad format",
    )
    campaign_id: int = pydantic.Field(
        ...,
        description="Campaign ID",
    )
    cost_type: "AdsAdCostType" = pydantic.Field(
        ...,
        description="",
    )
    description: str = pydantic.Field(
        ...,
        description="Ad description",
    )
    id: int = pydantic.Field(
        ...,
        description="Ad ID",
    )
    image_src: str = pydantic.Field(
        ...,
        description="Image URL",
    )
    image_src_2x: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image in double size",
    )
    link_domain: typing.Optional[str] = pydantic.Field(
        None,
        description="Domain of advertised object",
    )
    link_url: str = pydantic.Field(
        ...,
        description="URL of advertised object",
    )
    preview_link: typing.Optional[typing.Union[int, str,]] = pydantic.Field(
        None,
        description="link to preview an ad as it is shown on the website",
    )
    title: str = pydantic.Field(
        ...,
        description="Ad title",
    )
    video: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the ad is a video",
    )


class AdsCampaign(pydantic.BaseModel):
    all_limit: str = pydantic.Field(
        ...,
        description="Campaign's total limit, rubles",
    )
    day_limit: str = pydantic.Field(
        ...,
        description="Campaign's day limit, rubles",
    )
    id: int = pydantic.Field(
        ...,
        description="Campaign ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Campaign title",
    )
    start_time: int = pydantic.Field(
        ...,
        description="Campaign start time, as Unixtime",
    )
    status: "AdsCampaignStatus" = pydantic.Field(
        ...,
        description="",
    )
    stop_time: int = pydantic.Field(
        ...,
        description="Campaign stop time, as Unixtime",
    )
    type: "AdsCampaignType" = pydantic.Field(
        ...,
        description="",
    )


class AdsCategory(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Category ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Category name",
    )
    subcategories: typing.Optional[typing.List["BaseObjectWithName"]] = pydantic.Field(
        None,
        description="",
    )


class AdsClient(pydantic.BaseModel):
    all_limit: str = pydantic.Field(
        ...,
        description="Client's total limit, rubles",
    )
    day_limit: str = pydantic.Field(
        ...,
        description="Client's day limit, rubles",
    )
    id: int = pydantic.Field(
        ...,
        description="Client ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Client name",
    )


class AdsCriteria(pydantic.BaseModel):
    age_from: typing.Optional[int] = pydantic.Field(
        None,
        description="Age from",
    )
    age_to: typing.Optional[int] = pydantic.Field(
        None,
        description="Age to",
    )
    apps: typing.Optional[str] = pydantic.Field(
        None,
        description="Apps IDs",
    )
    apps_not: typing.Optional[str] = pydantic.Field(
        None,
        description="Apps IDs to except",
    )
    birthday: typing.Optional[int] = pydantic.Field(
        None,
        description="Days to birthday",
    )
    cities: typing.Optional[str] = pydantic.Field(
        None,
        description="Cities IDs",
    )
    cities_not: typing.Optional[str] = pydantic.Field(
        None,
        description="Cities IDs to except",
    )
    country: typing.Optional[int] = pydantic.Field(
        None,
        description="Country ID",
    )
    districts: typing.Optional[str] = pydantic.Field(
        None,
        description="Districts IDs",
    )
    groups: typing.Optional[str] = pydantic.Field(
        None,
        description="Communities IDs",
    )
    interest_categories: typing.Optional[str] = pydantic.Field(
        None,
        description="Interests categories IDs",
    )
    interests: typing.Optional[str] = pydantic.Field(
        None,
        description="Interests",
    )
    paying: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user has proceeded VK payments before",
    )
    positions: typing.Optional[str] = pydantic.Field(
        None,
        description="Positions IDs",
    )
    religions: typing.Optional[str] = pydantic.Field(
        None,
        description="Religions IDs",
    )
    retargeting_groups: typing.Optional[str] = pydantic.Field(
        None,
        description="Retargeting groups IDs",
    )
    retargeting_groups_not: typing.Optional[str] = pydantic.Field(
        None,
        description="Retargeting groups IDs to except",
    )
    school_from: typing.Optional[int] = pydantic.Field(
        None,
        description="School graduation year from",
    )
    school_to: typing.Optional[int] = pydantic.Field(
        None,
        description="School graduation year to",
    )
    schools: typing.Optional[str] = pydantic.Field(
        None,
        description="Schools IDs",
    )
    sex: typing.Optional["AdsCriteriaSex"] = pydantic.Field(
        None,
        description="",
    )
    stations: typing.Optional[str] = pydantic.Field(
        None,
        description="Stations IDs",
    )
    statuses: typing.Optional[str] = pydantic.Field(
        None,
        description="Relationship statuses",
    )
    streets: typing.Optional[str] = pydantic.Field(
        None,
        description="Streets IDs",
    )
    travellers: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="Travellers only",
    )
    uni_from: typing.Optional[int] = pydantic.Field(
        None,
        description="University graduation year from",
    )
    uni_to: typing.Optional[int] = pydantic.Field(
        None,
        description="University graduation year to",
    )
    user_browsers: typing.Optional[str] = pydantic.Field(
        None,
        description="Browsers",
    )
    user_devices: typing.Optional[str] = pydantic.Field(
        None,
        description="Devices",
    )
    user_os: typing.Optional[str] = pydantic.Field(
        None,
        description="Operating systems",
    )


class AdsDemoStats(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Object ID",
    )
    stats: typing.Optional["AdsDemostatsFormat"] = pydantic.Field(
        None,
        description="",
    )
    type: typing.Optional["AdsObjectType"] = pydantic.Field(
        None,
        description="",
    )


class AdsFloodStats(pydantic.BaseModel):
    left: int = pydantic.Field(
        ...,
        description="Requests left",
    )
    refresh: int = pydantic.Field(
        ...,
        description="Time to refresh in seconds",
    )


class AdsLinkStatus(pydantic.BaseModel):
    description: str = pydantic.Field(
        ...,
        description="Reject reason",
    )
    redirect_url: str = pydantic.Field(
        ...,
        description="URL",
    )
    status: str = pydantic.Field(
        ...,
        description="Link status",
    )


class AdsLookalikeRequest(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Lookalike request ID",
    )
    create_time: int = pydantic.Field(
        ...,
        description="Lookalike request create time, as Unixtime",
    )
    update_time: int = pydantic.Field(
        ...,
        description="Lookalike request update time, as Unixtime",
    )
    scheduled_delete_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Time by which lookalike request would be deleted, as Unixtime",
    )
    status: str = pydantic.Field(
        ...,
        description="Lookalike request status",
    )
    source_type: str = pydantic.Field(
        ...,
        description="Lookalike request source type",
    )
    source_retargeting_group_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Retargeting group id, which was used as lookalike seed",
    )
    source_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Lookalike request seed name (retargeting group name)",
    )
    audience_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Lookalike request seed audience size",
    )
    save_audience_levels: typing.Optional[
        typing.List["AdsLookalikeRequestSaveAudienceLevel"]
    ] = pydantic.Field(
        None,
        description="",
    )


class AdsLookalikeRequestSaveAudienceLevel(pydantic.BaseModel):
    level: typing.Optional[int] = pydantic.Field(
        None,
        description="Save audience level id, which is used in save audience queries",
    )
    audience_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Saved audience audience size for according level",
    )


class AdsMusician(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Targeting music artist ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Music artist name",
    )


class AdsParagraphs(pydantic.BaseModel):
    paragraph: typing.Optional[str] = pydantic.Field(
        None,
        description="Rules paragraph",
    )


class AdsPromotedPostReach(pydantic.BaseModel):
    hide: int = pydantic.Field(
        ...,
        description="Hides amount",
    )
    id: int = pydantic.Field(
        ...,
        description="Object ID from 'ids' parameter",
    )
    join_group: int = pydantic.Field(
        ...,
        description="Community joins",
    )
    links: int = pydantic.Field(
        ...,
        description="Link clicks",
    )
    reach_subscribers: int = pydantic.Field(
        ...,
        description="Subscribers reach",
    )
    reach_total: int = pydantic.Field(
        ...,
        description="Total reach",
    )
    report: int = pydantic.Field(
        ...,
        description="Reports amount",
    )
    to_group: int = pydantic.Field(
        ...,
        description="Community clicks",
    )
    unsubscribe: int = pydantic.Field(
        ...,
        description="'Unsubscribe' events amount",
    )
    video_views_100p: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views for 100 percent",
    )
    video_views_25p: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views for 25 percent",
    )
    video_views_3s: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views for 3 seconds",
    )
    video_views_50p: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views for 50 percent",
    )
    video_views_75p: typing.Optional[int] = pydantic.Field(
        None,
        description="Video views for 75 percent",
    )
    video_views_start: typing.Optional[int] = pydantic.Field(
        None,
        description="Video starts",
    )


class AdsRejectReason(pydantic.BaseModel):
    comment: typing.Optional[str] = pydantic.Field(
        None,
        description="Comment text",
    )
    rules: typing.Optional[typing.List["AdsRules"]] = pydantic.Field(
        None,
        description="",
    )


class AdsRules(pydantic.BaseModel):
    paragraphs: typing.Optional[typing.List["AdsParagraphs"]] = pydantic.Field(
        None,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Comment",
    )


class AdsStats(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Object ID",
    )
    stats: typing.Optional["AdsStatsFormat"] = pydantic.Field(
        None,
        description="",
    )
    type: typing.Optional["AdsObjectType"] = pydantic.Field(
        None,
        description="",
    )
    views_times: typing.Optional["AdsStatsViewsTimes"] = pydantic.Field(
        None,
        description="",
    )


class AdsStatsAge(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Impressions rate",
    )
    value: typing.Optional[str] = pydantic.Field(
        None,
        description="Age interval",
    )


class AdsStatsCities(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Impressions rate",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="City name",
    )
    value: typing.Optional[int] = pydantic.Field(
        None,
        description="City ID",
    )


class AdsStatsSex(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Impressions rate",
    )
    value: typing.Optional["AdsStatsSexValue"] = pydantic.Field(
        None,
        description="",
    )


class AdsStatsSexAge(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Impressions rate",
    )
    value: typing.Optional[str] = pydantic.Field(
        None,
        description="Sex and age interval",
    )


class AdsTargStats(pydantic.BaseModel):
    audience_count: int = pydantic.Field(
        ...,
        description="Audience",
    )
    recommended_cpc: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPC value for 50% reach (old format)",
    )
    recommended_cpm: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPM value for 50% reach (old format)",
    )
    recommended_cpc_50: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPC value for 50% reach",
    )
    recommended_cpm_50: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPM value for 50% reach",
    )
    recommended_cpc_70: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPC value for 70% reach",
    )
    recommended_cpm_70: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPM value for 70% reach",
    )
    recommended_cpc_90: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPC value for 90% reach",
    )
    recommended_cpm_90: typing.Optional[int] = pydantic.Field(
        None,
        description="Recommended CPM value for 90% reach",
    )


class AdsTargSuggestions(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Object ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Object name",
    )


class AdsTargSuggestionsCities(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Object ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Object name",
    )
    parent: typing.Optional[str] = pydantic.Field(
        None,
        description="Parent object",
    )


class AdsTargSuggestionsRegions(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Object ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Object name",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Object type",
    )


class AdsTargSuggestionsSchools(pydantic.BaseModel):
    desc: typing.Optional[str] = pydantic.Field(
        None,
        description="Full school title",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="School ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="School title",
    )
    parent: typing.Optional[str] = pydantic.Field(
        None,
        description="City name",
    )
    type: typing.Optional["AdsTargSuggestionsSchoolsType"] = pydantic.Field(
        None,
        description="",
    )


class AdsTargetGroup(pydantic.BaseModel):
    audience_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Audience",
    )
    domain: typing.Optional[str] = pydantic.Field(
        None,
        description="Site domain",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Group ID",
    )
    lifetime: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of days for user to be in group",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Group name",
    )
    pixel: typing.Optional[str] = pydantic.Field(
        None,
        description="Pixel code",
    )


class AdsUpdateOfficeUsersResult(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    is_success: bool = pydantic.Field(
        ...,
        description="",
    )
    error: typing.Optional["BaseError"] = pydantic.Field(
        None,
        description="",
    )


class AdsUserSpecification(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    role: "AdsAccessRolePublic" = pydantic.Field(
        ...,
        description="",
    )
    grant_access_to_all_clients: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    client_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    view_budget: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )


class AdsUserSpecificationCutted(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    role: "AdsAccessRolePublic" = pydantic.Field(
        ...,
        description="",
    )
    client_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    view_budget: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )


class AdsUsers(pydantic.BaseModel):
    accesses: typing.List["AdsAccesses"] = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="User ID",
    )


class AdswebGetAdCategoriesResponseCategoriesCategory(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    name: str = pydantic.Field(
        ...,
        description="",
    )


class AdswebGetAdUnitsResponseAdUnitsAdUnit(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    site_id: int = pydantic.Field(
        ...,
        description="",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class AdswebGetFraudHistoryResponseEntriesEntry(pydantic.BaseModel):
    site_id: int = pydantic.Field(
        ...,
        description="",
    )
    day: str = pydantic.Field(
        ...,
        description="",
    )


class AdswebGetSitesResponseSitesSite(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    status_user: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    status_moder: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    domains: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class AdswebGetStatisticsResponseItemsItem(pydantic.BaseModel):
    site_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    ad_unit_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    overall_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    months_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    month_min: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    month_max: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    days_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    day_min: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    day_max: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    hours_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    hour_min: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    hour_max: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class AppWidgetsPhoto(pydantic.BaseModel):
    id: str = pydantic.Field(
        ...,
        description="Image ID",
    )
    images: typing.List["BaseImage"] = pydantic.Field(
        ...,
        description="",
    )


class AppWidgetsPhotos(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    items: typing.Optional[typing.List["AppWidgetsPhoto"]] = pydantic.Field(
        None,
        description="",
    )


class AppsLeaderboard(pydantic.BaseModel):
    level: typing.Optional[int] = pydantic.Field(
        None,
        description="Level",
    )
    points: typing.Optional[int] = pydantic.Field(
        None,
        description="Points number",
    )
    score: typing.Optional[int] = pydantic.Field(
        None,
        description="Score number",
    )
    user_id: int = pydantic.Field(
        ...,
        description="User ID",
    )


class AppsScope(pydantic.BaseModel):
    name: str = pydantic.Field(
        ...,
        description="Scope name",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Scope title",
    )


class BaseCropPhoto(pydantic.BaseModel):
    photo: "PhotosPhoto" = pydantic.Field(
        ...,
        description="",
    )
    crop: "BaseCropPhotoCrop" = pydantic.Field(
        ...,
        description="",
    )
    rect: "BaseCropPhotoRect" = pydantic.Field(
        ...,
        description="",
    )


class BaseGradientPoint(pydantic.BaseModel):
    color: str = pydantic.Field(
        ...,
        description="Hex color code without #",
    )
    position: int = pydantic.Field(
        ...,
        description="Point position",
    )


class BaseImage(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    height: int = pydantic.Field(
        ...,
        description="Image height",
    )
    url: str = pydantic.Field(
        ...,
        description="Image url",
    )
    width: int = pydantic.Field(
        ...,
        description="Image width",
    )


class BaseMessageError(pydantic.BaseModel):
    code: typing.Optional[int] = pydantic.Field(
        None,
        description="Error code",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Error message",
    )


class BaseObject(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Object ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Object title",
    )


class BaseObjectWithName(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Object ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Object name",
    )


class BaseRequestParam(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None,
        description="Parameter name",
    )
    value: typing.Optional[str] = pydantic.Field(
        None,
        description="Parameter value",
    )


class BaseStickerAnimation(pydantic.BaseModel):
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Type of animation script",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of animation script",
    )


class BaseUploadServer(pydantic.BaseModel):
    upload_url: str = pydantic.Field(
        ...,
        description="Upload URL",
    )


class BaseUserId(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class BoardTopicComment(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the comment has been added in Unixtime",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Author ID",
    )
    id: int = pydantic.Field(
        ...,
        description="Comment ID",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None,
        description="Real position of the comment",
    )
    text: str = pydantic.Field(
        ...,
        description="Comment text",
    )
    can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can edit the comment",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )


class BoardTopicPoll(pydantic.BaseModel):
    answer_id: int = pydantic.Field(
        ...,
        description="Current user's answer ID",
    )
    answers: typing.List["PollsAnswer"] = pydantic.Field(
        ...,
        description="",
    )
    created: int = pydantic.Field(
        ...,
        description="Date when poll has been created in Unixtime",
    )
    is_closed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the poll is closed",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Poll owner's ID",
    )
    poll_id: int = pydantic.Field(
        ...,
        description="Poll ID",
    )
    question: str = pydantic.Field(
        ...,
        description="Poll question",
    )
    votes: str = pydantic.Field(
        ...,
        description="Votes number",
    )


class CallbackBoardPostDelete(pydantic.BaseModel):
    topic_owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    topic_id: int = pydantic.Field(
        ...,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackConfirmationMessage(pydantic.BaseModel):
    type: "CallbackMessageType" = pydantic.Field(
        ...,
        description="",
    )
    group_id: int = pydantic.Field(
        ...,
        description="",
    )
    secret: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class CallbackDonutMoneyWithdraw(pydantic.BaseModel):
    amount: int = pydantic.Field(
        ...,
        description="",
    )
    amount_without_fee: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackDonutMoneyWithdrawError(pydantic.BaseModel):
    reason: str = pydantic.Field(
        ...,
        description="",
    )


class CallbackDonutSubscriptionCancelled(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class CallbackDonutSubscriptionCreate(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    amount: int = pydantic.Field(
        ...,
        description="",
    )
    amount_without_fee: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackDonutSubscriptionExpired(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class CallbackDonutSubscriptionPriceChanged(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    amount_old: int = pydantic.Field(
        ...,
        description="",
    )
    amount_new: int = pydantic.Field(
        ...,
        description="",
    )
    amount_diff: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    amount_diff_without_fee: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class CallbackDonutSubscriptionProlonged(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    amount: int = pydantic.Field(
        ...,
        description="",
    )
    amount_without_fee: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackGroupChangePhoto(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    photo: "PhotosPhoto" = pydantic.Field(
        ...,
        description="",
    )


class CallbackGroupChangeSettings(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    self: "BaseBoolInt" = pydantic.Field(
        ...,
        description="",
    )


class CallbackGroupJoin(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    join_type: "CallbackGroupJoinType" = pydantic.Field(
        ...,
        description="",
    )


class CallbackGroupLeave(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    self: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )


class CallbackGroupOfficersEdit(pydantic.BaseModel):
    admin_id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    level_old: "CallbackGroupOfficerRole" = pydantic.Field(
        ...,
        description="",
    )
    level_new: "CallbackGroupOfficerRole" = pydantic.Field(
        ...,
        description="",
    )


class CallbackGroupSettingsChanges(pydantic.BaseModel):
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    access: typing.Optional["GroupsGroupIsClosed"] = pydantic.Field(
        None,
        description="",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    public_category: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    public_subcategory: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = pydantic.Field(
        None,
        description="",
    )
    website: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    enable_status_default: typing.Optional["GroupsGroupWall"] = pydantic.Field(
        None,
        description="",
    )
    enable_audio: typing.Optional["GroupsGroupAudio"] = pydantic.Field(
        None,
        description="",
    )
    enable_video: typing.Optional["GroupsGroupVideo"] = pydantic.Field(
        None,
        description="",
    )
    enable_photo: typing.Optional["GroupsGroupPhotos"] = pydantic.Field(
        None,
        description="",
    )
    enable_market: typing.Optional["CallbackGroupMarket"] = pydantic.Field(
        None,
        description="",
    )


class CallbackLikeAddRemove(pydantic.BaseModel):
    liker_id: int = pydantic.Field(
        ...,
        description="",
    )
    object_type: str = pydantic.Field(
        ...,
        description="",
    )
    object_owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    object_id: int = pydantic.Field(
        ...,
        description="",
    )
    post_id: int = pydantic.Field(
        ...,
        description="",
    )
    thread_reply_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class CallbackMarketComment(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    from_id: int = pydantic.Field(
        ...,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    market_owner_od: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    photo_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class CallbackMarketCommentDelete(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    item_id: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackMessageAllow(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    key: str = pydantic.Field(
        ...,
        description="",
    )


class CallbackMessageBase(pydantic.BaseModel):
    type: "CallbackMessageType" = pydantic.Field(
        ...,
        description="",
    )
    object: dict = pydantic.Field(
        ...,
        description="",
    )
    group_id: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackMessageDeny(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackPhotoComment(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    from_id: int = pydantic.Field(
        ...,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="",
    )
    text: str = pydantic.Field(
        ...,
        description="",
    )
    photo_owner_od: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackPhotoCommentDelete(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    photo_id: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackPollVoteNew(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    poll_id: int = pydantic.Field(
        ...,
        description="",
    )
    option_id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackQrScan(pydantic.BaseModel):
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    data: str = pydantic.Field(
        ...,
        description="",
    )
    type: str = pydantic.Field(
        ...,
        description="",
    )
    subtype: str = pydantic.Field(
        ...,
        description="",
    )
    reread: bool = pydantic.Field(
        ...,
        description="",
    )


class CallbackUserBlock(pydantic.BaseModel):
    admin_id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    unblock_date: int = pydantic.Field(
        ...,
        description="",
    )
    reason: int = pydantic.Field(
        ...,
        description="",
    )
    comment: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class CallbackUserUnblock(pydantic.BaseModel):
    admin_id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    by_end_date: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackVideoComment(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    from_id: int = pydantic.Field(
        ...,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="",
    )
    text: str = pydantic.Field(
        ...,
        description="",
    )
    video_owner_od: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackVideoCommentDelete(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    video_id: int = pydantic.Field(
        ...,
        description="",
    )


class CallbackWallCommentDelete(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    post_id: int = pydantic.Field(
        ...,
        description="",
    )


class DatabaseFaculty(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Faculty ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Faculty title",
    )


class DatabaseRegion(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Region ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Region title",
    )


class DatabaseSchool(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="School ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="School title",
    )


class DatabaseStation(pydantic.BaseModel):
    city_id: typing.Optional[int] = pydantic.Field(
        None,
        description="City ID",
    )
    color: typing.Optional[str] = pydantic.Field(
        None,
        description="Hex color code without #",
    )
    id: int = pydantic.Field(
        ...,
        description="Station ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Station name",
    )


class DatabaseUniversity(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="University ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="University title",
    )


class DocsDocPreviewPhotoSizes(pydantic.BaseModel):
    src: str = pydantic.Field(
        ...,
        description="URL of the image",
    )
    width: int = pydantic.Field(
        ...,
        description="Width in px",
    )
    height: int = pydantic.Field(
        ...,
        description="Height in px",
    )
    type: "PhotosPhotoSizesType" = pydantic.Field(
        ...,
        description="",
    )


class DocsDocTypes(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Doc type ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Doc type title",
    )
    count: int = pydantic.Field(
        ...,
        description="Number of docs",
    )


class DocsDocUploadResponse(pydantic.BaseModel):
    file: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded file data",
    )


class DonutDonatorSubscriptionInfo(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    next_payment_date: int = pydantic.Field(
        ...,
        description="",
    )
    amount: int = pydantic.Field(
        ...,
        description="",
    )
    status: str = pydantic.Field(
        ...,
        description="",
    )


class FaveBookmark(pydantic.BaseModel):
    added_date: int = pydantic.Field(
        ...,
        description="Timestamp, when this item was bookmarked",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    post: typing.Optional["WallWallpostFull"] = pydantic.Field(
        None,
        description="",
    )
    product: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None,
        description="",
    )
    seen: bool = pydantic.Field(
        ...,
        description="Has user seen this item",
    )
    tags: typing.List["FaveTag"] = pydantic.Field(
        ...,
        description="",
    )
    type: "FaveBookmarkType" = pydantic.Field(
        ...,
        description="Item type",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="",
    )


class FavePage(pydantic.BaseModel):
    description: str = pydantic.Field(
        ...,
        description="Some info about user or group",
    )
    group: typing.Optional["GroupsGroupFull"] = pydantic.Field(
        None,
        description="",
    )
    tags: typing.List["FaveTag"] = pydantic.Field(
        ...,
        description="",
    )
    type: "FavePageType" = pydantic.Field(
        ...,
        description="Item type",
    )
    updated_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Timestamp, when this page was bookmarked",
    )
    user: typing.Optional["UsersUserFull"] = pydantic.Field(
        None,
        description="",
    )


class FaveTag(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Tag id",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Tag name",
    )


class FriendsFriendStatus(pydantic.BaseModel):
    friend_status: "FriendsFriendStatusStatus" = pydantic.Field(
        ...,
        description="",
    )
    sign: typing.Optional[str] = pydantic.Field(
        None,
        description="MD5 hash for the result validation",
    )
    user_id: int = pydantic.Field(
        ...,
        description="User ID",
    )


class FriendsFriendsList(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="List ID",
    )
    name: str = pydantic.Field(
        ...,
        description="List title",
    )


class FriendsMutualFriend(pydantic.BaseModel):
    common_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Total mutual friends number",
    )
    common_friends: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class FriendsRequests(pydantic.BaseModel):
    from_: typing.Optional[str] = pydantic.Field(
        None,
        description="ID of the user by whom friend has been suggested",
        alias="from",
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = pydantic.Field(
        None,
        description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class FriendsRequestsXtrMessage(pydantic.BaseModel):
    from_: typing.Optional[str] = pydantic.Field(
        None,
        description="ID of the user by whom friend has been suggested",
        alias="from",
    )
    message: typing.Optional[str] = pydantic.Field(
        None,
        description="Message sent with a request",
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = pydantic.Field(
        None,
        description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class GiftsGift(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when gist has been sent in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Gift sender ID",
    )
    gift: typing.Optional["GiftsLayout"] = pydantic.Field(
        None,
        description="",
    )
    gift_hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Hash",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Gift ID",
    )
    message: typing.Optional[str] = pydantic.Field(
        None,
        description="Comment text",
    )
    privacy: typing.Optional["GiftsGiftPrivacy"] = pydantic.Field(
        None,
        description="",
    )


class GroupsAddress(pydantic.BaseModel):
    additional_address: typing.Optional[str] = pydantic.Field(
        None,
        description="Additional address to the place (6 floor, left door)",
    )
    address: typing.Optional[str] = pydantic.Field(
        None,
        description="String address to the place (Nevsky, 28)",
    )
    city_id: typing.Optional[int] = pydantic.Field(
        None,
        description="City id of address",
    )
    country_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Country id of address",
    )
    distance: typing.Optional[int] = pydantic.Field(
        None,
        description="Distance from the point",
    )
    id: int = pydantic.Field(
        ...,
        description="Address id",
    )
    latitude: typing.Optional[int] = pydantic.Field(
        None,
        description="Address latitude",
    )
    longitude: typing.Optional[int] = pydantic.Field(
        None,
        description="Address longitude",
    )
    metro_station_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Metro id of address",
    )
    phone: typing.Optional[str] = pydantic.Field(
        None,
        description="Address phone",
    )
    time_offset: typing.Optional[int] = pydantic.Field(
        None,
        description="Time offset int minutes from utc time",
    )
    timetable: typing.Optional["GroupsAddressTimetable"] = pydantic.Field(
        None,
        description="Week timetable for the address",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Title of the place (Zinger, etc)",
    )
    work_info_status: typing.Optional["GroupsAddressWorkInfoStatus"] = pydantic.Field(
        None,
        description="Status of information about timetable",
    )


class GroupsAddressesInfo(pydantic.BaseModel):
    is_enabled: bool = pydantic.Field(
        ...,
        description="Information whether addresses is enabled",
    )
    main_address_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Main address id for group",
    )


class GroupsBannedItem(pydantic.BaseModel):
    pass


class GroupsCallbackServer(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    title: str = pydantic.Field(
        ...,
        description="",
    )
    creator_id: int = pydantic.Field(
        ...,
        description="",
    )
    url: str = pydantic.Field(
        ...,
        description="",
    )
    secret_key: str = pydantic.Field(
        ...,
        description="",
    )
    status: str = pydantic.Field(
        ...,
        description="",
    )


class GroupsCallbackSettings(pydantic.BaseModel):
    api_version: typing.Optional[str] = pydantic.Field(
        None,
        description="API version used for the events",
    )
    events: typing.Optional["GroupsLongPollEvents"] = pydantic.Field(
        None,
        description="",
    )


class GroupsContactsItem(pydantic.BaseModel):
    desc: typing.Optional[str] = pydantic.Field(
        None,
        description="Contact description",
    )
    email: typing.Optional[str] = pydantic.Field(
        None,
        description="Contact email",
    )
    phone: typing.Optional[str] = pydantic.Field(
        None,
        description="Contact phone",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class GroupsCountersGroup(pydantic.BaseModel):
    addresses: typing.Optional[int] = pydantic.Field(
        None,
        description="Addresses number",
    )
    albums: typing.Optional[int] = pydantic.Field(
        None,
        description="Photo albums number",
    )
    audios: typing.Optional[int] = pydantic.Field(
        None,
        description="Audios number",
    )
    audio_playlists: typing.Optional[int] = pydantic.Field(
        None,
        description="Audio playlists number",
    )
    docs: typing.Optional[int] = pydantic.Field(
        None,
        description="Docs number",
    )
    market: typing.Optional[int] = pydantic.Field(
        None,
        description="Market items number",
    )
    photos: typing.Optional[int] = pydantic.Field(
        None,
        description="Photos number",
    )
    topics: typing.Optional[int] = pydantic.Field(
        None,
        description="Topics number",
    )
    videos: typing.Optional[int] = pydantic.Field(
        None,
        description="Videos number",
    )


class GroupsCover(pydantic.BaseModel):
    enabled: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether cover is enabled",
    )
    images: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupBanInfo(pydantic.BaseModel):
    comment: typing.Optional[str] = pydantic.Field(
        None,
        description="Ban comment",
    )
    end_date: typing.Optional[int] = pydantic.Field(
        None,
        description="End date of ban in Unixtime",
    )
    reason: typing.Optional["GroupsBanInfoReason"] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupCategory(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Category ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Category name",
    )
    subcategories: typing.Optional[typing.List["BaseObjectWithName"]] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupCategoryFull(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Category ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Category name",
    )
    page_count: int = pydantic.Field(
        ...,
        description="Pages number",
    )
    page_previews: typing.List["GroupsGroup"] = pydantic.Field(
        ...,
        description="",
    )
    subcategories: typing.Optional[typing.List["GroupsGroupCategory"]] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupCategoryType(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    name: str = pydantic.Field(
        ...,
        description="",
    )


class GroupsGroupLink(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Link label",
    )
    desc: typing.Optional[str] = pydantic.Field(
        None,
        description="Link description",
    )
    edit_title: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the title can be edited",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Link ID",
    )
    image_processing: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the image on processing",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="Link URL",
    )


class GroupsGroupPublicCategoryList(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    subcategories: typing.Optional[typing.List["GroupsGroupCategoryType"]] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupTag(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    name: str = pydantic.Field(
        ...,
        description="",
    )
    color: str = pydantic.Field(
        ...,
        description="",
    )
    uses: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupXtrInvitedBy(pydantic.BaseModel):
    admin_level: typing.Optional["GroupsGroupXtrInvitedByAdminLevel"] = pydantic.Field(
        None,
        description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Community ID",
    )
    invited_by: typing.Optional[int] = pydantic.Field(
        None,
        description="Inviter ID",
    )
    is_admin: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is manager",
    )
    is_advertiser: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is advertiser",
    )
    is_closed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community is closed",
    )
    is_member: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is member",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Community name",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 100 pixels in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 200 pixels in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 50 pixels in width",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Domain of the community page",
    )
    type: typing.Optional["GroupsGroupXtrInvitedByType"] = pydantic.Field(
        None,
        description="",
    )


class GroupsGroupsArray(pydantic.BaseModel):
    count: int = pydantic.Field(
        ...,
        description="Communities number",
    )
    items: typing.List[int] = pydantic.Field(
        ...,
        description="",
    )


class GroupsLinksItem(pydantic.BaseModel):
    desc: typing.Optional[str] = pydantic.Field(
        None,
        description="Link description",
    )
    edit_title: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the link title can be edited",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Link ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Link title",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square image of the link with 100 pixels in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square image of the link with 50 pixels in width",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="Link URL",
    )


class GroupsLiveCovers(pydantic.BaseModel):
    is_enabled: bool = pydantic.Field(
        ...,
        description="Information whether live covers is enabled",
    )
    is_scalable: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether live covers photo scaling is enabled",
    )
    story_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="",
    )


class GroupsLongPollServer(pydantic.BaseModel):
    key: str = pydantic.Field(
        ...,
        description="Long Poll key",
    )
    server: str = pydantic.Field(
        ...,
        description="Long Poll server address",
    )
    ts: str = pydantic.Field(
        ...,
        description="Number of the last event",
    )


class GroupsLongPollSettings(pydantic.BaseModel):
    api_version: typing.Optional[str] = pydantic.Field(
        None,
        description="API version used for the events",
    )
    events: "GroupsLongPollEvents" = pydantic.Field(
        ...,
        description="",
    )
    is_enabled: bool = pydantic.Field(
        ...,
        description="Shows whether Long Poll is enabled",
    )


class GroupsMarketInfo(pydantic.BaseModel):
    contact_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Contact person ID",
    )
    currency: typing.Optional["MarketCurrency"] = pydantic.Field(
        None,
        description="",
    )
    currency_text: typing.Optional[str] = pydantic.Field(
        None,
        description="Currency name",
    )
    enabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the market is enabled",
    )
    main_album_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Main market album ID",
    )
    price_max: typing.Optional[str] = pydantic.Field(
        None,
        description="Maximum price",
    )
    price_min: typing.Optional[str] = pydantic.Field(
        None,
        description="Minimum price",
    )


class GroupsMemberRole(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )
    permissions: typing.Optional[typing.List["GroupsMemberRolePermission"]] = pydantic.Field(
        None,
        description="",
    )
    role: typing.Optional["GroupsMemberRoleStatus"] = pydantic.Field(
        None,
        description="",
    )


class GroupsMemberStatus(pydantic.BaseModel):
    member: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether user is a member of the group",
    )
    user_id: int = pydantic.Field(
        ...,
        description="User ID",
    )


class GroupsMemberStatusFull(pydantic.BaseModel):
    can_invite: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether user can be invited",
    )
    can_recall: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether user's invite to the group can be recalled",
    )
    invitation: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether user has been invited to the group",
    )
    member: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether user is a member of the group",
    )
    request: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether user has send request to the group",
    )
    user_id: int = pydantic.Field(
        ...,
        description="User ID",
    )


class GroupsOnlineStatus(pydantic.BaseModel):
    minutes: typing.Optional[int] = pydantic.Field(
        None,
        description="Estimated time of answer (for status = answer_mark)",
    )
    status: "GroupsOnlineStatusType" = pydantic.Field(
        ...,
        description="",
    )


class GroupsOwnerXtrBanInfo(pydantic.BaseModel):
    ban_info: typing.Optional["GroupsBanInfo"] = pydantic.Field(
        None,
        description="",
    )
    group: typing.Optional["GroupsGroup"] = pydantic.Field(
        None,
        description="Information about group if type = group",
    )
    profile: typing.Optional["UsersUser"] = pydantic.Field(
        None,
        description="Information about group if type = profile",
    )
    type: typing.Optional["GroupsOwnerXtrBanInfoType"] = pydantic.Field(
        None,
        description="",
    )


class GroupsProfileItem(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="User id",
    )
    photo_50: str = pydantic.Field(
        ...,
        description="Url for user photo",
    )
    photo_100: str = pydantic.Field(
        ...,
        description="Url for user photo",
    )


class GroupsSettingsTwitter(pydantic.BaseModel):
    status: str = pydantic.Field(
        ...,
        description="",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class GroupsSubjectItem(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Subject ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Subject title",
    )


class GroupsTokenPermissionSetting(pydantic.BaseModel):
    name: str = pydantic.Field(
        ...,
        description="",
    )
    setting: int = pydantic.Field(
        ...,
        description="",
    )


class MarketMarketCategoryOld(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Category ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Category name",
    )
    section: "MarketSection" = pydantic.Field(
        ...,
        description="",
    )


class MarketMarketCategoryTree(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Category ID",
    )
    name: str = pydantic.Field(
        ...,
        description="Category name",
    )
    children: typing.Optional[typing.List["MarketMarketCategoryTree"]] = pydantic.Field(
        None,
        description="",
    )


class MarketOrder(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )
    group_id: int = pydantic.Field(
        ...,
        description="",
    )
    user_id: int = pydantic.Field(
        ...,
        description="",
    )
    display_order_id: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="",
    )
    status: int = pydantic.Field(
        ...,
        description="",
    )
    items_count: int = pydantic.Field(
        ...,
        description="",
    )
    track_number: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    track_link: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    comment: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    address: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    merchant_comment: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    weight: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    total_price: "MarketPrice" = pydantic.Field(
        ...,
        description="",
    )
    preview_order_items: typing.Optional[typing.List["MarketOrderItem"]] = pydantic.Field(
        None,
        description="Several order items for preview",
    )
    cancel_info: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="Information for cancel and revert order",
    )
    sku: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class MarketOrderItem(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ...,
        description="",
    )
    item_id: int = pydantic.Field(
        ...,
        description="",
    )
    price: "MarketPrice" = pydantic.Field(
        ...,
        description="",
    )
    quantity: int = pydantic.Field(
        ...,
        description="",
    )
    item: "MarketMarketItem" = pydantic.Field(
        ...,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    variants: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="",
    )
    sku: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class MessagesChat(pydantic.BaseModel):
    admin_id: int = pydantic.Field(
        ...,
        description="Chat creator ID",
    )
    id: int = pydantic.Field(
        ...,
        description="Chat ID",
    )
    kicked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Shows that user has been kicked from the chat",
    )
    left: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Shows that user has been left the chat",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 100 px in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 200 px in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 50 px in width",
    )
    push_settings: typing.Optional["MessagesChatPushSettings"] = pydantic.Field(
        None,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Chat title",
    )
    type: str = pydantic.Field(
        ...,
        description="Chat type",
    )
    users: typing.List[int] = pydantic.Field(
        ...,
        description="",
    )
    is_default_photo: typing.Optional[bool] = pydantic.Field(
        None,
        description="If provided photo is default",
    )


class MessagesChatFull(pydantic.BaseModel):
    admin_id: int = pydantic.Field(
        ...,
        description="Chat creator ID",
    )
    id: int = pydantic.Field(
        ...,
        description="Chat ID",
    )
    kicked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Shows that user has been kicked from the chat",
    )
    left: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Shows that user has been left the chat",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 100 px in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 200 px in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image with 50 px in width",
    )
    push_settings: typing.Optional["MessagesChatPushSettings"] = pydantic.Field(
        None,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Chat title",
    )
    type: str = pydantic.Field(
        ...,
        description="Chat type",
    )
    users: typing.List["MessagesUserXtrInvitedBy"] = pydantic.Field(
        ...,
        description="",
    )


class MessagesChatPreview(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    joined: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    local_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    members: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class MessagesChatRestrictions(pydantic.BaseModel):
    admins_promote_users: typing.Optional[bool] = pydantic.Field(
        None,
        description="Only admins can promote users to admins",
    )
    only_admins_edit_info: typing.Optional[bool] = pydantic.Field(
        None,
        description="Only admins can change chat info",
    )
    only_admins_edit_pin: typing.Optional[bool] = pydantic.Field(
        None,
        description="Only admins can edit pinned message",
    )
    only_admins_invite: typing.Optional[bool] = pydantic.Field(
        None,
        description="Only admins can invite users to this chat",
    )
    only_admins_kick: typing.Optional[bool] = pydantic.Field(
        None,
        description="Only admins can kick users from this chat",
    )


class MessagesConversationMember(pydantic.BaseModel):
    can_kick: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is it possible for user to kick this member",
    )
    invited_by: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    is_admin: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    is_owner: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    is_message_request: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    join_date: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    request_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Message request date",
    )
    member_id: int = pydantic.Field(
        ...,
        description="",
    )


class MessagesConversationWithMessage(pydantic.BaseModel):
    conversation: typing.Optional["MessagesConversation"] = pydantic.Field(
        None,
        description="",
    )
    last_message: typing.Optional["MessagesMessage"] = pydantic.Field(
        None,
        description="",
    )


class MessagesForward(pydantic.BaseModel):
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Messages owner_id",
    )
    peer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Messages peer_id",
    )
    conversation_message_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    message_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    is_reply: typing.Optional[bool] = pydantic.Field(
        None,
        description="If you need to reply to a message",
    )


class MessagesHistoryAttachment(pydantic.BaseModel):
    attachment: "MessagesHistoryMessageAttachment" = pydantic.Field(
        ...,
        description="",
    )
    message_id: int = pydantic.Field(
        ...,
        description="Message ID",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Message author's ID",
    )


class MessagesKeyboardButton(pydantic.BaseModel):
    action: "MessagesKeyboardButtonAction" = pydantic.Field(
        ...,
        description="",
    )
    color: typing.Optional[str] = pydantic.Field(
        None,
        description="Button color",
    )


class MessagesLastActivity(pydantic.BaseModel):
    online: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether user is online",
    )
    time: int = pydantic.Field(
        ...,
        description="Time when user was online in Unixtime",
    )


class MessagesLongpollMessages(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Total number",
    )
    items: typing.Optional[typing.List["MessagesMessage"]] = pydantic.Field(
        None,
        description="",
    )


class MessagesLongpollParams(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None,
        description="Key",
    )
    pts: typing.Optional[int] = pydantic.Field(
        None,
        description="Persistent timestamp",
    )
    server: typing.Optional[str] = pydantic.Field(
        None,
        description="Server URL",
    )
    ts: typing.Optional[str] = pydantic.Field(
        None,
        description="Timestamp",
    )


class MessagesMessageAttachment(pydantic.BaseModel):
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    audio_message: typing.Optional["MessagesAudioMessage"] = pydantic.Field(
        None,
        description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None,
        description="",
    )
    gift: typing.Optional["GiftsLayout"] = pydantic.Field(
        None,
        description="",
    )
    graffiti: typing.Optional["MessagesGraffiti"] = pydantic.Field(
        None,
        description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    market: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None,
        description="",
    )
    market_market_album: typing.Optional["MarketMarketAlbum"] = pydantic.Field(
        None,
        description="",
    )
    poll: typing.Optional["PollsPoll"] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    sticker: typing.Optional["BaseSticker"] = pydantic.Field(
        None,
        description="",
    )
    story: typing.Optional["StoriesStory"] = pydantic.Field(
        None,
        description="",
    )
    type: "MessagesMessageAttachmentType" = pydantic.Field(
        ...,
        description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="",
    )
    wall: typing.Optional["WallWallpostFull"] = pydantic.Field(
        None,
        description="",
    )
    wall_reply: typing.Optional["WallWallComment"] = pydantic.Field(
        None,
        description="",
    )


class MessagesMessagesArray(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    items: typing.Optional[typing.List["MessagesMessage"]] = pydantic.Field(
        None,
        description="",
    )


class MessagesPinnedMessage(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Unique auto-incremented number for all messages with this peer",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the message has been sent in Unixtime",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Message author's ID",
    )
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = pydantic.Field(
        None,
        description="Forwarded messages",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="Message ID",
    )
    peer_id: int = pydantic.Field(
        ...,
        description="Peer ID",
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = pydantic.Field(
        None,
        description="",
    )
    text: str = pydantic.Field(
        ...,
        description="Message text",
    )
    keyboard: typing.Optional["MessagesKeyboard"] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedEventActivity(pydantic.BaseModel):
    address: typing.Optional[str] = pydantic.Field(
        None,
        description="address of event",
    )
    button_text: str = pydantic.Field(
        ...,
        description="text of attach",
    )
    friends: typing.List[int] = pydantic.Field(
        ...,
        description="array of friends ids",
    )
    member_status: "GroupsGroupFullMemberStatus" = pydantic.Field(
        ...,
        description="Current user's member status",
    )
    text: str = pydantic.Field(
        ...,
        description="text of attach",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="event start time",
    )


class NewsfeedItemAudioAudio(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Audios number",
    )
    items: typing.Optional[typing.List["AudioAudio"]] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemBase(pydantic.BaseModel):
    type: "NewsfeedNewsfeedItemType" = pydantic.Field(
        ...,
        description="",
    )
    source_id: int = pydantic.Field(
        ...,
        description="Item source ID",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when item has been added in Unixtime",
    )


class NewsfeedItemDigestFooter(pydantic.BaseModel):
    style: str = pydantic.Field(
        ...,
        description="",
    )
    text: str = pydantic.Field(
        ...,
        description="text for invite to enable smart feed",
    )
    button: typing.Optional["NewsfeedItemDigestFooterButton"] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemDigestHeader(pydantic.BaseModel):
    title: str = pydantic.Field(
        ...,
        description="Title of the header",
    )
    subtitle: typing.Optional[str] = pydantic.Field(
        None,
        description="Subtitle of the header, when title have two strings",
    )
    style: str = pydantic.Field(
        ...,
        description="",
    )


class NewsfeedItemFriendFriends(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of friends has been added",
    )
    items: typing.Optional[typing.List["BaseUserId"]] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemHolidayRecommendationsBlockHeader(pydantic.BaseModel):
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Title of the header",
    )
    subtitle: typing.Optional[str] = pydantic.Field(
        None,
        description="Subtitle of the header",
    )
    image: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="",
    )
    action: typing.Optional["BaseLinkButtonAction"] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemPhotoPhotos(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Photos number",
    )
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemPhotoTagPhotoTags(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Tags number",
    )
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemPromoButtonAction(pydantic.BaseModel):
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    target: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemPromoButtonImage(pydantic.BaseModel):
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemVideoVideo(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Tags number",
    )
    items: typing.Optional[typing.List["VideoVideo"]] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemWallpostFeedback(pydantic.BaseModel):
    type: "NewsfeedItemWallpostFeedbackType" = pydantic.Field(
        ...,
        description="",
    )
    question: str = pydantic.Field(
        ...,
        description="",
    )
    answers: typing.Optional[typing.List["NewsfeedItemWallpostFeedbackAnswer"]] = pydantic.Field(
        None,
        description="",
    )
    stars_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    gratitude: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemWallpostFeedbackAnswer(pydantic.BaseModel):
    title: str = pydantic.Field(
        ...,
        description="",
    )
    id: str = pydantic.Field(
        ...,
        description="",
    )


class NewsfeedList(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="List ID",
    )
    title: str = pydantic.Field(
        ...,
        description="List title",
    )


class NotesNote(pydantic.BaseModel):
    read_comments: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the note",
    )
    comments: int = pydantic.Field(
        ...,
        description="Comments number",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the note has been created in Unixtime",
    )
    id: int = pydantic.Field(
        ...,
        description="Note ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Note owner's ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Note text",
    )
    text_wiki: typing.Optional[str] = pydantic.Field(
        None,
        description="Note text in wiki format",
    )
    title: str = pydantic.Field(
        ...,
        description="Note title",
    )
    view_url: str = pydantic.Field(
        ...,
        description="URL of the page with note preview",
    )


class NotesNoteComment(pydantic.BaseModel):
    date: int = pydantic.Field(
        ...,
        description="Date when the comment has beed added in Unixtime",
    )
    id: int = pydantic.Field(
        ...,
        description="Comment ID",
    )
    message: str = pydantic.Field(
        ...,
        description="Comment text",
    )
    nid: int = pydantic.Field(
        ...,
        description="Note ID",
    )
    oid: int = pydantic.Field(
        ...,
        description="Note ID",
    )
    reply_to: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of replied comment ",
    )
    uid: int = pydantic.Field(
        ...,
        description="Comment author's ID",
    )


class NotificationsNotification(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the event has been occurred",
    )
    feedback: typing.Optional["NotificationsFeedback"] = pydantic.Field(
        None,
        description="",
    )
    parent: typing.Optional["NotificationsNotificationParent"] = pydantic.Field(
        None,
        description="",
    )
    reply: typing.Optional["NotificationsReply"] = pydantic.Field(
        None,
        description="",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Notification type",
    )


class NotificationsNotificationsComment(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the comment has been added in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Comment ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Author ID",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    post: typing.Optional["WallWallpost"] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Comment text",
    )
    topic: typing.Optional["BoardTopic"] = pydantic.Field(
        None,
        description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="",
    )


class NotificationsSendMessageItem(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )
    status: typing.Optional[bool] = pydantic.Field(
        None,
        description="Notification status",
    )
    error: typing.Optional["NotificationsSendMessageError"] = pydantic.Field(
        None,
        description="",
    )


class OauthError(pydantic.BaseModel):
    error: str = pydantic.Field(
        ...,
        description="Error type",
    )
    error_description: str = pydantic.Field(
        ...,
        description="Error description",
    )
    redirect_uri: typing.Optional[str] = pydantic.Field(
        None,
        description="URI for validation",
    )


class OrdersAmount(pydantic.BaseModel):
    amounts: typing.Optional[typing.List["OrdersAmountItem"]] = pydantic.Field(
        None,
        description="",
    )
    currency: typing.Optional[str] = pydantic.Field(
        None,
        description="Currency name",
    )


class OrdersAmountItem(pydantic.BaseModel):
    amount: typing.Optional[int] = pydantic.Field(
        None,
        description="Votes amount in user's currency",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Amount description",
    )
    votes: typing.Optional[str] = pydantic.Field(
        None,
        description="Votes number",
    )


class OrdersOrder(pydantic.BaseModel):
    amount: typing.Optional[int] = pydantic.Field(
        None,
        description="Amount",
    )
    app_order_id: typing.Optional[int] = pydantic.Field(
        None,
        description="App order ID",
    )
    cancel_transaction_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Cancel transaction ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date of creation in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Order ID",
    )
    item: typing.Optional[str] = pydantic.Field(
        None,
        description="Order item",
    )
    receiver_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Receiver ID",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Order status",
    )
    transaction_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Transaction ID",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class OrdersSubscription(pydantic.BaseModel):
    cancel_reason: typing.Optional[str] = pydantic.Field(
        None,
        description="Cancel reason",
    )
    create_time: int = pydantic.Field(
        ...,
        description="Date of creation in Unixtime",
    )
    id: int = pydantic.Field(
        ...,
        description="Subscription ID",
    )
    item_id: str = pydantic.Field(
        ...,
        description="Subscription order item",
    )
    next_bill_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Date of next bill in Unixtime",
    )
    pending_cancel: typing.Optional[bool] = pydantic.Field(
        None,
        description="Pending cancel state",
    )
    period: int = pydantic.Field(
        ...,
        description="Subscription period",
    )
    period_start_time: int = pydantic.Field(
        ...,
        description="Date of last period start in Unixtime",
    )
    price: int = pydantic.Field(
        ...,
        description="Subscription price",
    )
    status: str = pydantic.Field(
        ...,
        description="Subscription status",
    )
    test_mode: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is test subscription",
    )
    trial_expire_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Date of trial expire in Unixtime",
    )
    update_time: int = pydantic.Field(
        ...,
        description="Date of last change in Unixtime",
    )


class OwnerState(pydantic.BaseModel):
    state: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="wiki text to describe user state",
    )


class PagesWikipage(pydantic.BaseModel):
    creator_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Page creator ID",
    )
    creator_name: typing.Optional[int] = pydantic.Field(
        None,
        description="Page creator name",
    )
    editor_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Last editor ID",
    )
    editor_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Last editor name",
    )
    group_id: int = pydantic.Field(
        ...,
        description="Community ID",
    )
    id: int = pydantic.Field(
        ...,
        description="Page ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Page title",
    )
    views: int = pydantic.Field(
        ...,
        description="Views number",
    )
    who_can_edit: "PagesPrivacySettings" = pydantic.Field(
        ...,
        description="Edit settings of the page",
    )
    who_can_view: "PagesPrivacySettings" = pydantic.Field(
        ...,
        description="View settings of the page",
    )


class PagesWikipageHistory(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Version ID",
    )
    length: int = pydantic.Field(
        ...,
        description="Page size in bytes",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the page has been edited in Unixtime",
    )
    editor_id: int = pydantic.Field(
        ...,
        description="Last editor ID",
    )
    editor_name: str = pydantic.Field(
        ...,
        description="Last editor name",
    )


class PhotosCommentXtrPid(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the comment has been added in Unixtime",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Author ID",
    )
    id: int = pydantic.Field(
        ...,
        description="Comment ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )
    pid: int = pydantic.Field(
        ...,
        description="Photo ID",
    )
    reply_to_comment: typing.Optional[int] = pydantic.Field(
        None,
        description="Replied comment ID",
    )
    reply_to_user: typing.Optional[int] = pydantic.Field(
        None,
        description="Replied user ID",
    )
    text: str = pydantic.Field(
        ...,
        description="Comment text",
    )
    parents_stack: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    thread: typing.Optional["CommentThread"] = pydantic.Field(
        None,
        description="",
    )


class PhotosImage(pydantic.BaseModel):
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Height of the photo in px.",
    )
    type: typing.Optional["PhotosImageType"] = pydantic.Field(
        None,
        description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo URL.",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Width of the photo in px.",
    )


class PhotosMarketAlbumUploadResponse(pydantic.BaseModel):
    gid: typing.Optional[int] = pydantic.Field(
        None,
        description="Community ID",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None,
        description="Upload server number",
    )


class PhotosMarketUploadResponse(pydantic.BaseModel):
    crop_data: typing.Optional[str] = pydantic.Field(
        None,
        description="Crop data",
    )
    crop_hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Crop hash",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Community ID",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None,
        description="Upload server number",
    )


class PhotosMessageUploadResponse(pydantic.BaseModel):
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None,
        description="Upload server number",
    )


class PhotosOwnerUploadResponse(pydantic.BaseModel):
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None,
        description="Upload server number",
    )


class PhotosPhotoAlbumFull(pydantic.BaseModel):
    can_upload: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can upload photo to the album",
    )
    comments_disabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether album comments are disabled",
    )
    created: int = pydantic.Field(
        ...,
        description="Date when the album has been created in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo album description",
    )
    id: int = pydantic.Field(
        ...,
        description="Photo album ID",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Album owner's ID",
    )
    size: int = pydantic.Field(
        ...,
        description="Photos number",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None,
        description="",
    )
    thumb_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Thumb photo ID",
    )
    thumb_is_last: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the album thumb is last photo",
    )
    thumb_src: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the thumb image",
    )
    title: str = pydantic.Field(
        ...,
        description="Photo album title",
    )
    updated: int = pydantic.Field(
        ...,
        description="Date when the album has been updated last time in Unixtime",
    )
    upload_by_admins_only: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether only community administrators can upload photos",
    )


class PhotosPhotoFull(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the photo",
    )
    album_id: int = pydantic.Field(
        ...,
        description="Album ID",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the photo",
    )
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo height",
    )
    id: int = pydantic.Field(
        ...,
        description="Photo ID",
    )
    images: typing.Optional[typing.List["PhotosImage"]] = pydantic.Field(
        None,
        description="",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None,
        description="Latitude",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None,
        description="",
    )
    long: typing.Optional[int] = pydantic.Field(
        None,
        description="Longitude",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Photo owner's ID",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    reposts: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    tags: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo width",
    )


class PhotosPhotoFullXtrRealOffset(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the photo",
    )
    album_id: int = pydantic.Field(
        ...,
        description="Album ID",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo height",
    )
    hidden: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="Returns if the photo is hidden above the wall",
    )
    id: int = pydantic.Field(
        ...,
        description="Photo ID",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None,
        description="Latitude",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None,
        description="",
    )
    long: typing.Optional[int] = pydantic.Field(
        None,
        description="Longitude",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Photo owner's ID",
    )
    photo_1280: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 1280 px width",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 130 px width",
    )
    photo_2560: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 2560 px width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 604 px width",
    )
    photo_75: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 75 px width",
    )
    photo_807: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 807 px width",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None,
        description="Real position of the photo",
    )
    reposts: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None,
        description="",
    )
    tags: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo width",
    )


class PhotosPhotoSizes(pydantic.BaseModel):
    height: int = pydantic.Field(
        ...,
        description="Height in px",
    )
    url: str = pydantic.Field(
        ...,
        description="URL of the image",
    )
    src: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the image",
    )
    type: "PhotosPhotoSizesType" = pydantic.Field(
        ...,
        description="",
    )
    width: int = pydantic.Field(
        ...,
        description="Width in px",
    )


class PhotosPhotoTag(pydantic.BaseModel):
    date: int = pydantic.Field(
        ...,
        description="Date when tag has been added in Unixtime",
    )
    id: int = pydantic.Field(
        ...,
        description="Tag ID",
    )
    placer_id: int = pydantic.Field(
        ...,
        description="ID of the tag creator",
    )
    tagged_name: str = pydantic.Field(
        ...,
        description="Tag description",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Tagged description.",
    )
    user_id: int = pydantic.Field(
        ...,
        description="Tagged user ID",
    )
    viewed: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Information whether the tag is reviewed",
    )
    x: int = pydantic.Field(
        ...,
        description="Coordinate X of the left upper corner",
    )
    x2: int = pydantic.Field(
        ...,
        description="Coordinate X of the right lower corner",
    )
    y: int = pydantic.Field(
        ...,
        description="Coordinate Y of the left upper corner",
    )
    y2: int = pydantic.Field(
        ...,
        description="Coordinate Y of the right lower corner",
    )


class PhotosPhotoUpload(pydantic.BaseModel):
    album_id: int = pydantic.Field(
        ...,
        description="Album ID",
    )
    upload_url: str = pydantic.Field(
        ...,
        description="URL to upload photo",
    )
    fallback_upload_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Fallback URL if upload_url returned error",
    )
    user_id: int = pydantic.Field(
        ...,
        description="User ID",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Group ID",
    )


class PhotosPhotoUploadResponse(pydantic.BaseModel):
    aid: typing.Optional[int] = pydantic.Field(
        None,
        description="Album ID",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded photo data",
    )
    photos_list: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded photos data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None,
        description="Upload server number",
    )


class PhotosPhotoXtrRealOffset(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the photo",
    )
    album_id: int = pydantic.Field(
        ...,
        description="Album ID",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo height",
    )
    hidden: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="Returns if the photo is hidden above the wall",
    )
    id: int = pydantic.Field(
        ...,
        description="Photo ID",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None,
        description="Latitude",
    )
    long: typing.Optional[int] = pydantic.Field(
        None,
        description="Longitude",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Photo owner's ID",
    )
    photo_1280: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 1280 px width",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 130 px width",
    )
    photo_2560: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 2560 px width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 604 px width",
    )
    photo_75: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 75 px width",
    )
    photo_807: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 807 px width",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None,
        description="Real position of the photo",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo width",
    )


class PhotosPhotoXtrTagInfo(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the photo",
    )
    album_id: int = pydantic.Field(
        ...,
        description="Album ID",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo height",
    )
    id: int = pydantic.Field(
        ...,
        description="Photo ID",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None,
        description="Latitude",
    )
    long: typing.Optional[int] = pydantic.Field(
        None,
        description="Longitude",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Photo owner's ID",
    )
    photo_1280: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 1280 px width",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 130 px width",
    )
    photo_2560: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 2560 px width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 604 px width",
    )
    photo_75: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 75 px width",
    )
    photo_807: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of image with 807 px width",
    )
    placer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the tag creator",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None,
        description="",
    )
    tag_created: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when tag has been added in Unixtime",
    )
    tag_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Tag ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Original photo width",
    )


class PhotosTagsSuggestionItem(pydantic.BaseModel):
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    caption: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    buttons: typing.Optional[typing.List["PhotosTagsSuggestionItemButton"]] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    tags: typing.Optional[typing.List["PhotosPhotoTag"]] = pydantic.Field(
        None,
        description="",
    )
    track_code: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class PhotosTagsSuggestionItemButton(pydantic.BaseModel):
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    action: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    style: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class PhotosWallUploadResponse(pydantic.BaseModel):
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None,
        description="Upload server number",
    )


class PollsAnswer(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="Answer ID",
    )
    rate: int = pydantic.Field(
        ...,
        description="Answer rate in percents",
    )
    text: str = pydantic.Field(
        ...,
        description="Answer text",
    )
    votes: int = pydantic.Field(
        ...,
        description="Votes number",
    )


class PollsFriend(pydantic.BaseModel):
    id: int = pydantic.Field(
        ...,
        description="",
    )


class PollsVoters(pydantic.BaseModel):
    answer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Answer ID",
    )
    users: typing.Optional["PollsVotersUsers"] = pydantic.Field(
        None,
        description="",
    )


class PrettyCardsPrettyCard(pydantic.BaseModel):
    button: typing.Optional[str] = pydantic.Field(
        None,
        description="Button key",
    )
    button_text: typing.Optional[str] = pydantic.Field(
        None,
        description="Button text in current language",
    )
    card_id: str = pydantic.Field(
        ...,
        description="Card ID (long int returned as string)",
    )
    images: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None,
        description="",
    )
    link_url: str = pydantic.Field(
        ...,
        description="Link URL",
    )
    photo: str = pydantic.Field(
        ...,
        description="Photo ID (format <owner_id>_<media_id>)",
    )
    price: typing.Optional[str] = pydantic.Field(
        None,
        description="Price if set (decimal number returned as string)",
    )
    price_old: typing.Optional[str] = pydantic.Field(
        None,
        description="Old price if set (decimal number returned as string)",
    )
    title: str = pydantic.Field(
        ...,
        description="Title",
    )


class SearchHint(pydantic.BaseModel):
    app: typing.Optional["AppsApp"] = pydantic.Field(
        None,
        description="",
    )
    description: str = pydantic.Field(
        ...,
        description="Object description",
    )
    global_: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the object has been found globally",
        alias="global",
    )
    group: typing.Optional["GroupsGroup"] = pydantic.Field(
        None,
        description="",
    )
    profile: typing.Optional["UsersUserMin"] = pydantic.Field(
        None,
        description="",
    )
    section: "SearchHintSection" = pydantic.Field(
        ...,
        description="",
    )
    type: "SearchHintType" = pydantic.Field(
        ...,
        description="",
    )


class SecureLevel(pydantic.BaseModel):
    level: typing.Optional[int] = pydantic.Field(
        None,
        description="Level",
    )
    uid: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class SecureSmsNotification(pydantic.BaseModel):
    app_id: typing.Optional[str] = pydantic.Field(
        None,
        description="Application ID",
    )
    date: typing.Optional[str] = pydantic.Field(
        None,
        description="Date when message has been sent in Unixtime",
    )
    id: typing.Optional[str] = pydantic.Field(
        None,
        description="Notification ID",
    )
    message: typing.Optional[str] = pydantic.Field(
        None,
        description="Messsage text",
    )
    user_id: typing.Optional[str] = pydantic.Field(
        None,
        description="User ID",
    )


class SecureTokenChecked(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when access_token has been generated in Unixtime",
    )
    expire: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when access_token will expire in Unixtime",
    )
    success: typing.Optional[int] = pydantic.Field(
        None,
        description="Returns if successfully processed",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )


class SecureTransaction(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Transaction date in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Transaction ID",
    )
    uid_from: typing.Optional[int] = pydantic.Field(
        None,
        description="From ID",
    )
    uid_to: typing.Optional[int] = pydantic.Field(
        None,
        description="To ID",
    )
    votes: typing.Optional[int] = pydantic.Field(
        None,
        description="Votes number",
    )


class StatsCity(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Visitors number",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="City name",
    )
    value: typing.Optional[int] = pydantic.Field(
        None,
        description="City ID",
    )


class StatsCountry(pydantic.BaseModel):
    code: typing.Optional[str] = pydantic.Field(
        None,
        description="Country code",
    )
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Visitors number",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Country name",
    )
    value: typing.Optional[int] = pydantic.Field(
        None,
        description="Country ID",
    )


class StatsPeriod(pydantic.BaseModel):
    activity: typing.Optional["StatsActivity"] = pydantic.Field(
        None,
        description="",
    )
    period_from: typing.Optional[int] = pydantic.Field(
        None,
        description="Unix timestamp",
    )
    period_to: typing.Optional[int] = pydantic.Field(
        None,
        description="Unix timestamp",
    )
    reach: typing.Optional["StatsReach"] = pydantic.Field(
        None,
        description="",
    )
    visitors: typing.Optional["StatsViews"] = pydantic.Field(
        None,
        description="",
    )


class StatsSexAge(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Visitors number",
    )
    value: str = pydantic.Field(
        ...,
        description="Sex/age value",
    )
    reach: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    reach_subscribers: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    count_subscribers: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class StatsWallpostStat(pydantic.BaseModel):
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    hide: typing.Optional[int] = pydantic.Field(
        None,
        description="Hidings number",
    )
    join_group: typing.Optional[int] = pydantic.Field(
        None,
        description="People have joined the group",
    )
    links: typing.Optional[int] = pydantic.Field(
        None,
        description="Link clickthrough",
    )
    reach_subscribers: typing.Optional[int] = pydantic.Field(
        None,
        description="Subscribers reach",
    )
    reach_subscribers_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    reach_total: typing.Optional[int] = pydantic.Field(
        None,
        description="Total reach",
    )
    reach_total_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    reach_viral: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    reach_ads: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    report: typing.Optional[int] = pydantic.Field(
        None,
        description="Reports number",
    )
    to_group: typing.Optional[int] = pydantic.Field(
        None,
        description="Clickthrough to community",
    )
    unsubscribe: typing.Optional[int] = pydantic.Field(
        None,
        description="Unsubscribed members",
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )


class StatusStatus(pydantic.BaseModel):
    text: str = pydantic.Field(
        ...,
        description="Status text",
    )
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )


class StorageValue(pydantic.BaseModel):
    key: str = pydantic.Field(
        ...,
        description="",
    )
    value: str = pydantic.Field(
        ...,
        description="",
    )


class StoriesClickableArea(pydantic.BaseModel):
    x: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    y: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class StoriesClickableSticker(pydantic.BaseModel):
    clickable_area: typing.List["StoriesClickableArea"] = pydantic.Field(
        ...,
        description="",
    )
    id: int = pydantic.Field(
        ...,
        description="Clickable sticker ID",
    )
    hashtag: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    link_object: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    mention: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    tooltip_text: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    story_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    question: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    question_button: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    place_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    market_item: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None,
        description="",
    )
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    audio_start_time: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    style: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    type: str = pydantic.Field(
        ...,
        description="",
    )
    subtype: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    post_owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    poll: typing.Optional["PollsPoll"] = pydantic.Field(
        None,
        description="",
    )
    color: typing.Optional[str] = pydantic.Field(
        None,
        description="Color, hex format",
    )
    sticker_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Sticker ID",
    )
    sticker_pack_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Sticker pack ID",
    )
    app: typing.Optional["AppsAppMin"] = pydantic.Field(
        None,
        description="",
    )
    app_context: typing.Optional[str] = pydantic.Field(
        None,
        description="Additional context for app sticker",
    )
    has_new_interactions: typing.Optional[bool] = pydantic.Field(
        None,
        description="Whether current user has unread interaction with this app",
    )
    is_broadcast_notify_allowed: typing.Optional[bool] = pydantic.Field(
        None,
        description="Whether current user allowed broadcast notify from this app",
    )


class StoriesFeedItem(pydantic.BaseModel):
    type: str = pydantic.Field(
        ...,
        description="Type of Feed Item",
    )
    id: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    stories: typing.Optional[typing.List["StoriesStory"]] = pydantic.Field(
        None,
        description="Author stories",
    )
    grouped: typing.Optional[typing.List["StoriesFeedItem"]] = pydantic.Field(
        None,
        description="Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)",
    )
    app: typing.Optional["AppsAppMin"] = pydantic.Field(
        None,
        description="App, which stories has been grouped (for type app_grouped_stories)",
    )
    promo_data: typing.Optional["StoriesPromoBlock"] = pydantic.Field(
        None,
        description="Additional data for promo stories (for type promo_stories)",
    )
    birthday_user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class StoriesStatLine(pydantic.BaseModel):
    name: str = pydantic.Field(
        ...,
        description="",
    )
    counter: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    is_unavailable: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )


class StoriesStoryStats(pydantic.BaseModel):
    answer: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )
    bans: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )
    open_link: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )
    replies: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )
    shares: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )
    subscribers: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )
    views: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )
    likes: "StoriesStoryStatsStat" = pydantic.Field(
        ...,
        description="",
    )


class StoriesViewersItem(pydantic.BaseModel):
    is_liked: bool = pydantic.Field(
        ...,
        description="user has like for this object",
    )
    user_id: int = pydantic.Field(
        ...,
        description="user id",
    )
    user: typing.Optional["UsersUserFull"] = pydantic.Field(
        None,
        description="",
    )


class UsersCareer(pydantic.BaseModel):
    city_id: typing.Optional[int] = pydantic.Field(
        None,
        description="City ID",
    )
    city_name: typing.Optional[str] = pydantic.Field(
        None,
        description="City name",
    )
    company: typing.Optional[str] = pydantic.Field(
        None,
        description="Company name",
    )
    country_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Country ID",
    )
    from_: typing.Optional[int] = pydantic.Field(None, description="From year", alias="from")
    group_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Community ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Career ID",
    )
    position: typing.Optional[str] = pydantic.Field(
        None,
        description="Position",
    )
    until: typing.Optional[int] = pydantic.Field(
        None,
        description="Till year",
    )


class UsersExports(pydantic.BaseModel):
    facebook: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    livejournal: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    twitter: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class UsersLastSeen(pydantic.BaseModel):
    platform: typing.Optional[int] = pydantic.Field(
        None,
        description="Type of the platform that used for the last authorization",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="Last visit date (in Unix time)",
    )


class UsersMilitary(pydantic.BaseModel):
    country_id: int = pydantic.Field(
        ...,
        description="Country ID",
    )
    from_: typing.Optional[int] = pydantic.Field(None, description="From year", alias="from")
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Military ID",
    )
    unit: str = pydantic.Field(
        ...,
        description="Unit name",
    )
    unit_id: int = pydantic.Field(
        ...,
        description="Unit ID",
    )
    until: typing.Optional[int] = pydantic.Field(
        None,
        description="Till year",
    )


class UsersOccupation(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of school, university, company group",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Name of occupation",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Type of occupation",
    )


class UsersOnlineInfo(pydantic.BaseModel):
    visible: bool = pydantic.Field(
        ...,
        description="Whether you can see real online status of user or not",
    )
    last_seen: typing.Optional[int] = pydantic.Field(
        None,
        description="Last time we saw user being active",
    )
    is_online: typing.Optional[bool] = pydantic.Field(
        None,
        description="Whether user is currently online or not",
    )
    app_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Application id from which user is currently online or was last seen online",
    )
    is_mobile: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is user online from desktop app or mobile app",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="In case user online is not visible, it indicates approximate timeframe of user online",
    )


class UsersRelative(pydantic.BaseModel):
    birth_date: typing.Optional[str] = pydantic.Field(
        None,
        description="Date of child birthday (format dd.mm.yyyy)",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Relative ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Name of relative",
    )
    type: str = pydantic.Field(
        ...,
        description="Relative type",
    )


class UsersSchool(pydantic.BaseModel):
    city: typing.Optional[int] = pydantic.Field(
        None,
        description="City ID",
    )
    class_: typing.Optional[str] = pydantic.Field(
        None, description="School class letter", alias="class"
    )
    country: typing.Optional[int] = pydantic.Field(
        None,
        description="Country ID",
    )
    id: typing.Optional[str] = pydantic.Field(
        None,
        description="School ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="School name",
    )
    type: typing.Optional[int] = pydantic.Field(
        None,
        description="School type ID",
    )
    type_str: typing.Optional[str] = pydantic.Field(
        None,
        description="School type name",
    )
    year_from: typing.Optional[int] = pydantic.Field(
        None,
        description="Year the user started to study",
    )
    year_graduated: typing.Optional[int] = pydantic.Field(
        None,
        description="Graduation year",
    )
    year_to: typing.Optional[int] = pydantic.Field(
        None,
        description="Year the user finished to study",
    )
    speciality: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class UsersUniversity(pydantic.BaseModel):
    chair: typing.Optional[int] = pydantic.Field(
        None,
        description="Chair ID",
    )
    chair_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Chair name",
    )
    city: typing.Optional[int] = pydantic.Field(
        None,
        description="City ID",
    )
    country: typing.Optional[int] = pydantic.Field(
        None,
        description="Country ID",
    )
    education_form: typing.Optional[str] = pydantic.Field(
        None,
        description="Education form",
    )
    education_status: typing.Optional[str] = pydantic.Field(
        None,
        description="Education status",
    )
    faculty: typing.Optional[int] = pydantic.Field(
        None,
        description="Faculty ID",
    )
    faculty_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Faculty name",
    )
    graduation: typing.Optional[int] = pydantic.Field(
        None,
        description="Graduation year",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="University ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="University name",
    )
    university_group_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class UsersUserCounters(pydantic.BaseModel):
    albums: typing.Optional[int] = pydantic.Field(
        None,
        description="Albums number",
    )
    audios: typing.Optional[int] = pydantic.Field(
        None,
        description="Audios number",
    )
    followers: typing.Optional[int] = pydantic.Field(
        None,
        description="Followers number",
    )
    friends: typing.Optional[int] = pydantic.Field(
        None,
        description="Friends number",
    )
    gifts: typing.Optional[int] = pydantic.Field(
        None,
        description="Gifts number",
    )
    groups: typing.Optional[int] = pydantic.Field(
        None,
        description="Communities number",
    )
    notes: typing.Optional[int] = pydantic.Field(
        None,
        description="Notes number",
    )
    online_friends: typing.Optional[int] = pydantic.Field(
        None,
        description="Online friends number",
    )
    pages: typing.Optional[int] = pydantic.Field(
        None,
        description="Public pages number",
    )
    photos: typing.Optional[int] = pydantic.Field(
        None,
        description="Photos number",
    )
    subscriptions: typing.Optional[int] = pydantic.Field(
        None,
        description="Subscriptions number",
    )
    user_photos: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of photos with user",
    )
    user_videos: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of videos with user",
    )
    videos: typing.Optional[int] = pydantic.Field(
        None,
        description="Videos number",
    )
    new_photo_tags: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    new_recognition_tags: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    mutual_friends: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    posts: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    articles: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    wishes: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    podcasts: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    clips: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    clips_followers: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )


class UsersUserSettingsXtr(pydantic.BaseModel):
    connections: typing.Optional["UsersUserConnections"] = pydantic.Field(
        None,
        description="",
    )
    bdate: typing.Optional[str] = pydantic.Field(
        None,
        description="User's date of birth",
    )
    bdate_visibility: typing.Optional[int] = pydantic.Field(
        None,
        description="Information whether user's birthdate are hidden",
    )
    city: typing.Optional["BaseCity"] = pydantic.Field(
        None,
        description="",
    )
    country: typing.Optional["BaseCountry"] = pydantic.Field(
        None,
        description="",
    )
    first_name: typing.Optional[str] = pydantic.Field(
        None,
        description="User first name",
    )
    home_town: str = pydantic.Field(
        ...,
        description="User's hometown",
    )
    last_name: typing.Optional[str] = pydantic.Field(
        None,
        description="User last name",
    )
    maiden_name: typing.Optional[str] = pydantic.Field(
        None,
        description="User maiden name",
    )
    name_request: typing.Optional["AccountNameRequest"] = pydantic.Field(
        None,
        description="",
    )
    personal: typing.Optional["UsersPersonal"] = pydantic.Field(
        None,
        description="",
    )
    phone: typing.Optional[str] = pydantic.Field(
        None,
        description="User phone number with some hidden digits",
    )
    relation: typing.Optional["UsersUserRelation"] = pydantic.Field(
        None,
        description="User relationship status",
    )
    relation_partner: typing.Optional["UsersUserMin"] = pydantic.Field(
        None,
        description="",
    )
    relation_pending: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether relation status is pending",
    )
    relation_requests: typing.Optional[typing.List["UsersUserMin"]] = pydantic.Field(
        None,
        description="",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Domain name of the user's page",
    )
    sex: typing.Optional["BaseSex"] = pydantic.Field(
        None,
        description="User sex",
    )
    status: str = pydantic.Field(
        ...,
        description="User status",
    )
    status_audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    interests: typing.Optional["AccountUserSettingsInterests"] = pydantic.Field(
        None,
        description="",
    )
    languages: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="",
    )


class UsersUsersArray(pydantic.BaseModel):
    count: int = pydantic.Field(
        ...,
        description="Users number",
    )
    items: typing.List[int] = pydantic.Field(
        ...,
        description="",
    )


class UtilsDomainResolved(pydantic.BaseModel):
    object_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Object ID",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Group ID",
    )
    type: typing.Optional["UtilsDomainResolvedType"] = pydantic.Field(
        None,
        description="",
    )


class UtilsLastShortenedLink(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for private stats",
    )
    key: typing.Optional[str] = pydantic.Field(
        None,
        description="Link key (characters after vk.cc/)",
    )
    short_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Short link URL",
    )
    timestamp: typing.Optional[int] = pydantic.Field(
        None,
        description="Creation time in Unixtime",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="Full URL",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Total views number",
    )


class UtilsLinkChecked(pydantic.BaseModel):
    link: typing.Optional[str] = pydantic.Field(
        None,
        description="Link URL",
    )
    status: typing.Optional["UtilsLinkCheckedStatus"] = pydantic.Field(
        None,
        description="",
    )


class UtilsLinkStats(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None,
        description="Link key (characters after vk.cc/)",
    )
    stats: typing.Optional[typing.List["UtilsStats"]] = pydantic.Field(
        None,
        description="",
    )


class UtilsLinkStatsExtended(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None,
        description="Link key (characters after vk.cc/)",
    )
    stats: typing.Optional[typing.List["UtilsStatsExtended"]] = pydantic.Field(
        None,
        description="",
    )


class UtilsShortLink(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for private stats",
    )
    key: typing.Optional[str] = pydantic.Field(
        None,
        description="Link key (characters after vk.cc/)",
    )
    short_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Short link URL",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="Full URL",
    )


class UtilsStats(pydantic.BaseModel):
    timestamp: typing.Optional[int] = pydantic.Field(
        None,
        description="Start time",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Total views number",
    )


class UtilsStatsCity(pydantic.BaseModel):
    city_id: typing.Optional[int] = pydantic.Field(
        None,
        description="City ID",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Views number",
    )


class UtilsStatsCountry(pydantic.BaseModel):
    country_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Country ID",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Views number",
    )


class UtilsStatsExtended(pydantic.BaseModel):
    cities: typing.Optional[typing.List["UtilsStatsCity"]] = pydantic.Field(
        None,
        description="",
    )
    countries: typing.Optional[typing.List["UtilsStatsCountry"]] = pydantic.Field(
        None,
        description="",
    )
    sex_age: typing.Optional[typing.List["UtilsStatsSexAge"]] = pydantic.Field(
        None,
        description="",
    )
    timestamp: typing.Optional[int] = pydantic.Field(
        None,
        description="Start time",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Total views number",
    )


class UtilsStatsSexAge(pydantic.BaseModel):
    age_range: typing.Optional[str] = pydantic.Field(
        None,
        description="Age denotation",
    )
    female: typing.Optional[int] = pydantic.Field(
        None,
        description=" Views by female users",
    )
    male: typing.Optional[int] = pydantic.Field(
        None,
        description=" Views by male users",
    )


class VideoLiveInfo(pydantic.BaseModel):
    enabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    is_notifications_blocked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )


class VideoLiveSettings(pydantic.BaseModel):
    can_rewind: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="If user car rewind live or not",
    )
    is_endless: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="If live is endless or not",
    )
    max_duration: typing.Optional[int] = pydantic.Field(
        None,
        description="Max possible time for rewind",
    )


class VideoSaveResult(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Video access key",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Video description",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Video owner ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Video title",
    )
    upload_url: typing.Optional[str] = pydantic.Field(
        None,
        description="URL for the video uploading",
    )
    video_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Video ID",
    )


class VideoVideoAlbumFull(pydantic.BaseModel):
    count: int = pydantic.Field(
        ...,
        description="Total number of videos in album",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Album ID",
    )
    image: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None,
        description="Album cover image in different sizes",
    )
    image_blur: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="Need blur album thumb or not",
    )
    is_system: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="Information whether album is system",
    )
    owner_id: int = pydantic.Field(
        ...,
        description="Album owner's ID",
    )
    title: str = pydantic.Field(
        ...,
        description="Album title",
    )
    updated_time: int = pydantic.Field(
        ...,
        description="Date when the album has been updated last time in Unixtime",
    )


class VideoVideoFiles(pydantic.BaseModel):
    external: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the external player",
    )
    mp4_240: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the mpeg4 file with 240p quality",
    )
    mp4_360: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the mpeg4 file with 360p quality",
    )
    mp4_480: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the mpeg4 file with 480p quality",
    )
    mp4_720: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the mpeg4 file with 720p quality",
    )
    mp4_1080: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the mpeg4 file with 1080p quality",
    )
    flv_320: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the flv file with 320p quality",
    )


class WallCarouselBase(pydantic.BaseModel):
    carousel_offset: typing.Optional[int] = pydantic.Field(
        None,
        description="Index of current carousel element",
    )


class WallCommentAttachment(pydantic.BaseModel):
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None,
        description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    market: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None,
        description="",
    )
    market_market_album: typing.Optional["MarketMarketAlbum"] = pydantic.Field(
        None,
        description="",
    )
    note: typing.Optional["WallAttachedNote"] = pydantic.Field(
        None,
        description="",
    )
    page: typing.Optional["PagesWikipageFull"] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    sticker: typing.Optional["BaseSticker"] = pydantic.Field(
        None,
        description="",
    )
    type: "WallCommentAttachmentType" = pydantic.Field(
        ...,
        description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="",
    )


class WallWallpostAttachment(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Access key for the audio",
    )
    album: typing.Optional["PhotosPhotoAlbum"] = pydantic.Field(
        None,
        description="",
    )
    app: typing.Optional["WallAppPost"] = pydantic.Field(
        None,
        description="",
    )
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None,
        description="",
    )
    event: typing.Optional["EventsEventAttach"] = pydantic.Field(
        None,
        description="",
    )
    group: typing.Optional["GroupsGroupAttach"] = pydantic.Field(
        None,
        description="",
    )
    graffiti: typing.Optional["WallGraffiti"] = pydantic.Field(
        None,
        description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="",
    )
    market: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None,
        description="",
    )
    market_album: typing.Optional["MarketMarketAlbum"] = pydantic.Field(
        None,
        description="",
    )
    note: typing.Optional["WallAttachedNote"] = pydantic.Field(
        None,
        description="",
    )
    page: typing.Optional["PagesWikipageFull"] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    photos_list: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="",
    )
    poll: typing.Optional["PollsPoll"] = pydantic.Field(
        None,
        description="",
    )
    posted_photo: typing.Optional["WallPostedPhoto"] = pydantic.Field(
        None,
        description="",
    )
    type: "WallWallpostAttachmentType" = pydantic.Field(
        ...,
        description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None,
        description="",
    )


class WallWallpostDonut(pydantic.BaseModel):
    is_donut: bool = pydantic.Field(
        ...,
        description="Post only for dons",
    )
    paid_duration: typing.Optional[int] = pydantic.Field(
        None,
        description="Value of this field need to pass in wall.post/edit in donut_paid_duration",
    )
    placeholder: typing.Optional["WallWallpostDonutPlaceholder"] = pydantic.Field(
        None,
        description="If placeholder was respond, text and all attachments will be hidden",
    )
    can_publish_free_copy: typing.Optional[bool] = pydantic.Field(
        None,
        description="Says whether group admin can post free copy of this donut post",
    )
    edit_mode: typing.Optional[str] = pydantic.Field(
        None,
        description="Says what user can edit in post about donut properties",
    )


class WallWallpostToId(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None,
        description="",
    )
    copy_owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the source post owner",
    )
    copy_post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the source post",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date of publishing in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post author ID",
    )
    geo: typing.Optional["WallGeo"] = pydantic.Field(
        None,
        description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the post in favorites list",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="wall post ID (if comment)",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None,
        description="",
    )
    post_type: typing.Optional["WallPostType"] = pydantic.Field(
        None,
        description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None,
        description="",
    )
    signer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post signer ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Post text",
    )
    to_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Wall owner's ID",
    )


class WidgetsCommentRepliesItem(pydantic.BaseModel):
    cid: typing.Optional[int] = pydantic.Field(
        None,
        description="Comment ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the comment has been added in Unixtime",
    )
    likes: typing.Optional["WidgetsWidgetLikes"] = pydantic.Field(
        None,
        description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Comment text",
    )
    uid: typing.Optional[int] = pydantic.Field(
        None,
        description="User ID",
    )
    user: typing.Optional["UsersUserFull"] = pydantic.Field(
        None,
        description="",
    )


class WidgetsWidgetComment(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    can_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can delete the comment",
    )
    comments: typing.Optional["WidgetsCommentReplies"] = pydantic.Field(
        None,
        description="",
    )
    date: int = pydantic.Field(
        ...,
        description="Date when the comment has been added in Unixtime",
    )
    from_id: int = pydantic.Field(
        ...,
        description="Comment author ID",
    )
    id: int = pydantic.Field(
        ...,
        description="Comment ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )
    media: typing.Optional["WidgetsCommentMedia"] = pydantic.Field(
        None,
        description="",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None,
        description="",
    )
    post_type: int = pydantic.Field(
        ...,
        description="Post type",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None,
        description="",
    )
    text: str = pydantic.Field(
        ...,
        description="Comment text",
    )
    to_id: int = pydantic.Field(
        ...,
        description="Wall owner",
    )
    user: typing.Optional["UsersUserFull"] = pydantic.Field(
        None,
        description="",
    )


class WidgetsWidgetPage(pydantic.BaseModel):
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when widgets on the page has been initialized firstly in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Page description",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Page ID",
    )
    likes: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    page_id: typing.Optional[str] = pydantic.Field(
        None,
        description="page_id parameter value",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the preview image",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Page title",
    )
    url: typing.Optional[str] = pydantic.Field(
        None,
        description="Page absolute URL",
    )


class UsersUser(UsersUserMin):
    sex: typing.Optional["BaseSex"] = pydantic.Field(
        None,
        description="User sex",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Domain name of the user's page",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the user with 50 pixels in width",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the user with 100 pixels in width",
    )
    online_info: typing.Optional["UsersOnlineInfo"] = pydantic.Field(
        None,
        description="",
    )
    online: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user is online",
    )
    online_mobile: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user is online in mobile site or application",
    )
    online_app: typing.Optional[int] = pydantic.Field(
        None,
        description="Application ID",
    )
    verified: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user is verified",
    )
    trending: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user has a fire pictogram.",
    )
    friend_status: typing.Optional["FriendsFriendStatusStatus"] = pydantic.Field(
        None,
        description="",
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = pydantic.Field(
        None,
        description="",
    )


class UsersUserFull(UsersUser):
    first_name_nom: typing.Optional[str] = pydantic.Field(
        None,
        description="User's first name in nominative case",
    )
    first_name_gen: typing.Optional[str] = pydantic.Field(
        None,
        description="User's first name in genitive case",
    )
    first_name_dat: typing.Optional[str] = pydantic.Field(
        None,
        description="User's first name in dative case",
    )
    first_name_acc: typing.Optional[str] = pydantic.Field(
        None,
        description="User's first name in accusative case",
    )
    first_name_ins: typing.Optional[str] = pydantic.Field(
        None,
        description="User's first name in instrumental case",
    )
    first_name_abl: typing.Optional[str] = pydantic.Field(
        None,
        description="User's first name in prepositional case",
    )
    last_name_nom: typing.Optional[str] = pydantic.Field(
        None,
        description="User's last name in nominative case",
    )
    last_name_gen: typing.Optional[str] = pydantic.Field(
        None,
        description="User's last name in genitive case",
    )
    last_name_dat: typing.Optional[str] = pydantic.Field(
        None,
        description="User's last name in dative case",
    )
    last_name_acc: typing.Optional[str] = pydantic.Field(
        None,
        description="User's last name in accusative case",
    )
    last_name_ins: typing.Optional[str] = pydantic.Field(
        None,
        description="User's last name in instrumental case",
    )
    last_name_abl: typing.Optional[str] = pydantic.Field(
        None,
        description="User's last name in prepositional case",
    )
    nickname: typing.Optional[str] = pydantic.Field(
        None,
        description="User nickname",
    )
    maiden_name: typing.Optional[str] = pydantic.Field(
        None,
        description="User maiden name",
    )
    domain: typing.Optional[str] = pydantic.Field(
        None,
        description="Domain name of the user's page",
    )
    bdate: typing.Optional[str] = pydantic.Field(
        None,
        description="User's date of birth",
    )
    city: typing.Optional["BaseCity"] = pydantic.Field(
        None,
        description="",
    )
    country: typing.Optional["BaseCountry"] = pydantic.Field(
        None,
        description="",
    )
    timezone: typing.Optional[int] = pydantic.Field(
        None,
        description="User's timezone",
    )
    owner_state: typing.Optional["OwnerState"] = pydantic.Field(
        None,
        description="",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the user with 200 pixels in width",
    )
    photo_max: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the user with maximum width",
    )
    photo_200_orig: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of user's photo with 200 pixels in width",
    )
    photo_400_orig: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of user's photo with 400 pixels in width",
    )
    photo_max_orig: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of user's photo of maximum size",
    )
    photo_id: typing.Optional[str] = pydantic.Field(
        None,
        description="ID of the user's main photo",
    )
    has_photo: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user has main photo",
    )
    has_mobile: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user specified his phone number",
    )
    is_friend: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user is a friend of current user",
    )
    wall_comments: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment wall posts",
    )
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can post on the user's wall",
    )
    can_see_all_posts: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see other users' audio on the wall",
    )
    can_see_audio: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see the user's audio",
    )
    type: typing.Optional["UsersUserType"] = pydantic.Field(
        None,
        description="",
    )
    email: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    skype: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    facebook: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    facebook_name: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    twitter: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    livejournal: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    instagram: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    test: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    video_live: typing.Optional["VideoLiveInfo"] = pydantic.Field(
        None,
        description="",
    )
    is_video_live_notifications_blocked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    is_service: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )
    service_description: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_rec: typing.Optional["PhotosPhotoFalseable"] = pydantic.Field(
        None,
        description="",
    )
    photo_medium: typing.Optional["PhotosPhotoFalseable"] = pydantic.Field(
        None,
        description="",
    )
    photo_medium_rec: typing.Optional["PhotosPhotoFalseable"] = pydantic.Field(
        None,
        description="",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_big: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_400: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    photo_max_size: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None,
        description="",
    )
    language: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    stories_archive_count: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    wall_default: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    can_call: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether current user can call",
    )
    can_see_wishes: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether current user can see the user's wishes",
    )
    can_see_gifts: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see the user's gifts",
    )
    interests: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    books: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    tv: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    quotes: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    about: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    games: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    movies: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    activities: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    music: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    can_write_private_message: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can write private message",
    )
    can_send_friend_request: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can send a friend request",
    )
    can_be_invited_group: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether current user can be invited to the community",
    )
    mobile_phone: typing.Optional[str] = pydantic.Field(
        None,
        description="User's mobile phone number",
    )
    home_phone: typing.Optional[str] = pydantic.Field(
        None,
        description="User's additional phone number",
    )
    site: typing.Optional[str] = pydantic.Field(
        None,
        description="User's website",
    )
    status_audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="User's status",
    )
    activity: typing.Optional[str] = pydantic.Field(
        None,
        description="User's status",
    )
    last_seen: typing.Optional["UsersLastSeen"] = pydantic.Field(
        None,
        description="",
    )
    exports: typing.Optional["UsersExports"] = pydantic.Field(
        None,
        description="",
    )
    crop_photo: typing.Optional["BaseCropPhoto"] = pydantic.Field(
        None,
        description="",
    )
    followers_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of user's followers",
    )
    video_live_level: typing.Optional[int] = pydantic.Field(
        None,
        description="User level in live streams achievements",
    )
    video_live_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of user's live streams",
    )
    clips_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of user's clips",
    )
    blacklisted: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is in the requested user's blacklist.",
    )
    blacklisted_by_me: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the requested user is in current user's blacklist",
    )
    is_favorite: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the requested user is in faves of current user",
    )
    is_hidden_from_feed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the requested user is hidden from current user's newsfeed",
    )
    common_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of common friends with current user",
    )
    occupation: typing.Optional["UsersOccupation"] = pydantic.Field(
        None,
        description="",
    )
    career: typing.Optional[typing.List["UsersCareer"]] = pydantic.Field(
        None,
        description="",
    )
    military: typing.Optional[typing.List["UsersMilitary"]] = pydantic.Field(
        None,
        description="",
    )
    university: typing.Optional[int] = pydantic.Field(
        None,
        description="University ID",
    )
    university_name: typing.Optional[str] = pydantic.Field(
        None,
        description="University name",
    )
    university_group_id: typing.Optional[int] = pydantic.Field(
        None,
        description="",
    )
    faculty: typing.Optional[int] = pydantic.Field(
        None,
        description="Faculty ID",
    )
    faculty_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Faculty name",
    )
    graduation: typing.Optional[int] = pydantic.Field(
        None,
        description="Graduation year",
    )
    education_form: typing.Optional[str] = pydantic.Field(
        None,
        description="Education form",
    )
    education_status: typing.Optional[str] = pydantic.Field(
        None,
        description="User's education status",
    )
    home_town: typing.Optional[str] = pydantic.Field(
        None,
        description="User hometown",
    )
    relation: typing.Optional["UsersUserRelation"] = pydantic.Field(
        None,
        description="User relationship status",
    )
    relation_partner: typing.Optional["UsersUserMin"] = pydantic.Field(
        None,
        description="",
    )
    personal: typing.Optional["UsersPersonal"] = pydantic.Field(
        None,
        description="",
    )
    universities: typing.Optional[typing.List["UsersUniversity"]] = pydantic.Field(
        None,
        description="",
    )
    schools: typing.Optional[typing.List["UsersSchool"]] = pydantic.Field(
        None,
        description="",
    )
    relatives: typing.Optional[typing.List["UsersRelative"]] = pydantic.Field(
        None,
        description="",
    )
    is_subscribed_podcasts: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether current user is subscribed to podcasts",
    )
    can_subscribe_podcasts: typing.Optional[bool] = pydantic.Field(
        None,
        description="Owner in whitelist or not",
    )
    can_subscribe_posts: typing.Optional[bool] = pydantic.Field(
        None,
        description="Can subscribe to wall",
    )
    counters: typing.Optional["UsersUserCounters"] = pydantic.Field(
        None,
        description="",
    )
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    can_upload_doc: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    has_email: typing.Optional[bool] = pydantic.Field(
        None,
        description="",
    )



class UsersUserXtrType(UsersUser):
    type: typing.Optional["UsersUserType"] = pydantic.Field(
        None,
        description="",
    )


class AccountUserSettings(UsersUserSettingsXtr):
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the user with 200 pixels in width",
    )
    is_service_account: typing.Optional[bool] = pydantic.Field(
        None,
        description="flag about service account",
    )


class AdsTargSettings(AdsCriteria):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Ad ID",
    )
    campaign_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Campaign ID",
    )


class AppsApp(AppsAppMin):
    author_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Application author's URL",
    )
    banner_1120: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app banner with 1120 px in width",
    )
    banner_560: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app banner with 560 px in width",
    )
    icon_16: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the app icon with 16 px in width",
    )
    is_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Is new flag",
    )
    push_enabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Is push enabled",
    )
    screen_orientation: typing.Optional[int] = pydantic.Field(
        None,
        description="Screen orientation",
    )
    friends: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    catalog_position: typing.Optional[int] = pydantic.Field(
        None,
        description="Catalog position",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Application description",
    )
    genre: typing.Optional[str] = pydantic.Field(
        None,
        description="Genre name",
    )
    genre_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Genre ID",
    )
    international: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the application is multilanguage",
    )
    is_in_catalog: typing.Optional[int] = pydantic.Field(
        None,
        description="Information whether application is in mobile catalog",
    )
    leaderboard_type: typing.Optional["AppsAppLeaderboardType"] = pydantic.Field(
        None,
        description="",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Members number",
    )
    platform_id: typing.Optional[str] = pydantic.Field(
        None,
        description="Application ID in store",
    )
    published_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the application has been published in Unixtime",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Screen name",
    )
    section: typing.Optional[str] = pydantic.Field(
        None,
        description="Application section name",
    )


class DatabaseCity(BaseObject):
    area: typing.Optional[str] = pydantic.Field(
        None,
        description="Area title",
    )
    region: typing.Optional[str] = pydantic.Field(
        None,
        description="Region title",
    )
    important: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the city is included in important cities list",
    )


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    is_request_unread: typing.Optional[bool] = pydantic.Field(
        None,
        description="Is friend request from other user unread",
    )


class FriendsUserXtrLists(UsersUserFull):
    lists: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )


class FriendsUserXtrPhone(UsersUserFull):
    phone: typing.Optional[str] = pydantic.Field(
        None,
        description="User phone",
    )


class GroupsGroupFull(GroupsGroup):
    market: typing.Optional["GroupsMarketInfo"] = pydantic.Field(
        None,
        description="",
    )
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = pydantic.Field(
        None,
        description="Current user's member status",
    )
    is_adult: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community is adult",
    )
    is_hidden_from_feed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community is hidden from current user's newsfeed",
    )
    is_favorite: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community is in faves",
    )
    is_subscribed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is subscribed",
    )
    city: typing.Optional["BaseObject"] = pydantic.Field(
        None,
        description="",
    )
    country: typing.Optional["BaseCountry"] = pydantic.Field(
        None,
        description="",
    )
    verified: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community is verified",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Community description",
    )
    wiki_page: typing.Optional[str] = pydantic.Field(
        None,
        description="Community's main wiki page title",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Community members number",
    )
    video_live_level: typing.Optional[int] = pydantic.Field(
        None,
        description="Community level live streams achievements",
    )
    video_live_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of community's live streams",
    )
    clips_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of community's clips",
    )
    counters: typing.Optional["GroupsCountersGroup"] = pydantic.Field(
        None,
        description="",
    )
    cover: typing.Optional["GroupsCover"] = pydantic.Field(
        None,
        description="",
    )
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can post on community's wall",
    )
    can_see_all_posts: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see all posts on community's wall",
    )
    activity: typing.Optional[str] = pydantic.Field(
        None,
        description="Type of group, start date of event or category of public page",
    )
    fixed_post: typing.Optional[int] = pydantic.Field(
        None,
        description="Fixed post ID",
    )
    can_create_topic: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can create topic",
    )
    can_upload_doc: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can upload doc",
    )
    can_upload_story: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can upload story",
    )
    can_upload_video: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can upload video",
    )
    has_photo: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community has photo",
    )
    crop_photo: typing.Optional["BaseCropPhoto"] = pydantic.Field(
        None,
        description="Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Community status",
    )
    main_album_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Community's main photo album ID",
    )
    links: typing.Optional[typing.List["GroupsLinksItem"]] = pydantic.Field(
        None,
        description="",
    )
    contacts: typing.Optional[typing.List["GroupsContactsItem"]] = pydantic.Field(
        None,
        description="",
    )
    wall: typing.Optional[int] = pydantic.Field(
        None,
        description="Information about wall status in community",
    )
    site: typing.Optional[str] = pydantic.Field(
        None,
        description="Community's website",
    )
    main_section: typing.Optional["GroupsGroupFullMainSection"] = pydantic.Field(
        None,
        description="",
    )
    trending: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the community has a fire pictogram.",
    )
    can_message: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can send a message to community",
    )
    is_messages_blocked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community can send a message to current user",
    )
    can_send_notify: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community can send notifications by phone number to current user",
    )
    online_status: typing.Optional["GroupsOnlineStatus"] = pydantic.Field(
        None,
        description="Status of replies in community messages",
    )
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = pydantic.Field(
        None,
        description="Information whether age limit",
    )
    ban_info: typing.Optional["GroupsGroupBanInfo"] = pydantic.Field(
        None,
        description="User ban info",
    )
    has_market_app: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether community has installed market app",
    )
    addresses: typing.Optional["GroupsAddressesInfo"] = pydantic.Field(
        None,
        description="Info about addresses in groups",
    )
    is_subscribed_podcasts: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether current user is subscribed to podcasts",
    )
    can_subscribe_podcasts: typing.Optional[bool] = pydantic.Field(
        None,
        description="Owner in whitelist or not",
    )
    can_subscribe_posts: typing.Optional[bool] = pydantic.Field(
        None,
        description="Can subscribe to wall",
    )
    live_covers: typing.Optional["GroupsLiveCovers"] = pydantic.Field(
        None,
        description="Live covers state",
    )


class GroupsUserXtrRole(UsersUserFull, GroupsMemberRole):
    pass


class MarketMarketItemFull(MarketMarketItem):
    albums_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )
    photos: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None,
        description="",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current use can comment the item",
    )
    can_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current use can repost the item",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None,
        description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None,
        description="",
    )
    views_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Views number",
    )
    wishlist_item_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Object identifier in wishlist of viewer",
    )
    cancel_info: typing.Optional["BaseLink"] = pydantic.Field(
        None,
        description="Information for cancel and revert order",
    )
    user_agreement_info: typing.Optional[str] = pydantic.Field(
        None,
        description="User agreement info",
    )
    sku: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    invited_by: typing.Optional[int] = pydantic.Field(
        None,
        description="ID of the inviter",
    )


class NewsfeedItemAudio(NewsfeedItemBase):
    audio: typing.Optional["NewsfeedItemAudioAudio"] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )


class NewsfeedItemDigest(NewsfeedItemBase):
    feed_id: typing.Optional[str] = pydantic.Field(
        None,
        description="id of feed in digest",
    )
    items: typing.Optional[typing.List["WallWallpost"]] = pydantic.Field(
        None,
        description="",
    )
    main_post_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="",
    )
    template: typing.Optional[str] = pydantic.Field(
        None,
        description="type of digest",
    )
    header: typing.Optional["NewsfeedItemDigestHeader"] = pydantic.Field(
        None,
        description="",
    )
    footer: typing.Optional["NewsfeedItemDigestFooter"] = pydantic.Field(
        None,
        description="",
    )
    track_code: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemFriend(NewsfeedItemBase):
    friends: typing.Optional["NewsfeedItemFriendFriends"] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemPhoto(NewsfeedItemBase):
    photos: typing.Optional["NewsfeedItemPhotoPhotos"] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )


class NewsfeedItemPhotoTag(NewsfeedItemBase):
    photo_tags: typing.Optional["NewsfeedItemPhotoTagPhotoTags"] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )


class NewsfeedItemPromoButton(NewsfeedItemBase):
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    action: typing.Optional["NewsfeedItemPromoButtonAction"] = pydantic.Field(
        None,
        description="",
    )
    images: typing.Optional[typing.List["NewsfeedItemPromoButtonImage"]] = pydantic.Field(
        None,
        description="",
    )
    track_code: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemTopic(NewsfeedItemBase):
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None,
        description="",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Topic post ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Post text",
    )


class NewsfeedItemVideo(NewsfeedItemBase):
    video: typing.Optional["NewsfeedItemVideoVideo"] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedItemWallpost(NewsfeedItemBase):
    activity: typing.Optional["NewsfeedEventActivity"] = pydantic.Field(
        None,
        description="",
    )
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = pydantic.Field(
        None,
        description="",
    )
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None,
        description="",
    )
    copy_history: typing.Optional[typing.List["WallWallpost"]] = pydantic.Field(
        None,
        description="",
    )
    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = pydantic.Field(
        None,
        description="",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None,
        description="",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the post in favorites list",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None,
        description="",
    )
    marked_as_ads: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the post is marked as ads",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post ID",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None,
        description="",
    )
    post_type: typing.Optional["NewsfeedItemWallpostType"] = pydantic.Field(
        None,
        description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None,
        description="",
    )
    signer_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Post signer ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Post text",
    )
    views: typing.Optional["WallViews"] = pydantic.Field(
        None,
        description="Count of views",
    )
    short_text_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Preview length control parameter",
    )


class NewsfeedListFull(NewsfeedList):
    no_reposts: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether reposts hiding is enabled",
    )
    source_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None,
        description="",
    )


class NewsfeedNewsfeedItem(
    NewsfeedItemWallpost,
    NewsfeedItemPhoto,
    NewsfeedItemPhotoTag,
    NewsfeedItemFriend,
    NewsfeedItemAudio,
    NewsfeedItemVideo,
    NewsfeedItemTopic,
    NewsfeedItemDigest,
    NewsfeedItemPromoButton,
):
    pass


class NewsfeedNewsfeedPhoto(PhotosPhoto):
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None,
        description="",
    )
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None,
        description="",
    )
    can_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can repost the photo",
    )


class NotificationsNotificationParent(NotificationsNotificationsComment):
    pass


class PhotosPhotoFalseable(pydantic.BaseModel):
    pass


class UsersSubscriptionsItem(
    UsersUserXtrType,
    GroupsGroupFull,
):
    pass


class UsersUserXtrCounters(UsersUserFull):
    pass


class VideoVideo(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None,
        description="Video access key",
    )
    adding_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when the video has been added in Unixtime",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the video",
    )
    can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can edit the video",
    )
    can_like: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can like the video",
    )
    can_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can repost the video",
    )
    can_subscribe: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can subscribe to author of the video",
    )
    can_add_to_faves: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can add the video to favourites",
    )
    can_add: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can add the video",
    )
    can_attach_link: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can attach action button to the video",
    )
    is_private: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="1 if video is private",
    )
    comments: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of comments",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when video has been uploaded in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Video description",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None,
        description="Video duration in seconds",
    )
    image: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None,
        description="",
    )
    first_frame: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None,
        description="",
    )
    width: typing.Optional[int] = pydantic.Field(
        None,
        description="Video width",
    )
    height: typing.Optional[int] = pydantic.Field(
        None,
        description="Video height",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Video ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Video owner ID",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Id of the user who uploaded the video if it was uploaded to a group by member",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Video title",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="Whether video is added to bookmarks",
    )
    player: typing.Optional[str] = pydantic.Field(
        None,
        description="Video embed URL",
    )
    processing: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="Returns if the video is processing",
    )
    converting: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="1 if  video is being converted",
    )
    restriction: typing.Optional["MediaRestriction"] = pydantic.Field(
        None,
        description="",
    )
    added: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="1 if video is added to user's albums",
    )
    is_subscribed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="1 if user is subscribed to author of the video",
    )
    track_code: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    repeat: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="Information whether the video is repeated",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of views",
    )
    local_views: typing.Optional[int] = pydantic.Field(
        None,
        description="If video is external, number of views on vk",
    )
    content_restricted: typing.Optional[int] = pydantic.Field(
        None,
        description="Restriction code",
    )
    content_restricted_message: typing.Optional[str] = pydantic.Field(
        None,
        description="Restriction text",
    )
    balance: typing.Optional[int] = pydantic.Field(
        None,
        description="Live donations balance",
    )
    live_status: typing.Optional[str] = pydantic.Field(
        None,
        description="Live stream status",
    )
    live: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="1 if the video is a live stream",
    )
    upcoming: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="1 if the video is an upcoming stream",
    )
    live_start_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Date in Unixtime when the live stream is scheduled to start by the author",
    )
    live_notify: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)",
    )
    spectators: typing.Optional[int] = pydantic.Field(
        None,
        description="Number of spectators of the stream",
    )
    platform: typing.Optional[str] = pydantic.Field(
        None,
        description="External platform",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None,
        description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None,
        description="",
    )


class VideoVideoFull(VideoVideo):
    files: typing.Optional["VideoVideoFiles"] = pydantic.Field(
        None,
        description="",
    )
    live_settings: typing.Optional["VideoLiveSettings"] = pydantic.Field(
        None,
        description="Settings for live stream",
    )


class VideoVideoImage(BaseImage):
    with_padding: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None,
        description="",
    )


class WallWallpostFull(WallWallpost):
    copy_history: typing.Optional[typing.List["WallWallpost"]] = pydantic.Field(
        None,
        description="",
    )
    can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can edit the post",
    )
    created_by: typing.Optional[int] = pydantic.Field(
        None,
        description="Post creator ID (if post still can be edited)",
    )
    can_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can delete the post",
    )
    can_pin: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can pin the post",
    )
    donut: typing.Optional["WallWallpostDonut"] = pydantic.Field(
        None,
        description="",
    )
    is_pinned: typing.Optional[int] = pydantic.Field(
        None,
        description="Information whether the post is pinned",
    )
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None,
        description="",
    )
    marked_as_ads: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the post is marked as ads",
    )
    short_text_rate: typing.Optional[int] = pydantic.Field(
        None,
        description="Preview length control parameter",
    )


AccountNameRequest.update_forward_refs()
AccountPushConversations.update_forward_refs()
AccountPushParams.update_forward_refs()
AccountUserSettingsInterest.update_forward_refs()
AccountUserSettingsInterests.update_forward_refs()
AdsDemostatsFormat.update_forward_refs()
AdsStatsFormat.update_forward_refs()
AdsStatsViewsTimes.update_forward_refs()
AppsAppMin.update_forward_refs()
AudioAudio.update_forward_refs()
BaseCity.update_forward_refs()
BaseCommentsInfo.update_forward_refs()
BaseCountry.update_forward_refs()
BaseCropPhotoCrop.update_forward_refs()
BaseCropPhotoRect.update_forward_refs()
BaseError.update_forward_refs()
BaseGeo.update_forward_refs()
BaseGeoCoordinates.update_forward_refs()
BaseLikes.update_forward_refs()
BaseLikesInfo.update_forward_refs()
BaseLink.update_forward_refs()
BaseLinkApplication.update_forward_refs()
BaseLinkApplicationStore.update_forward_refs()
BaseLinkButton.update_forward_refs()
BaseLinkButtonAction.update_forward_refs()
BaseLinkProduct.update_forward_refs()
BaseLinkRating.update_forward_refs()
BaseObjectCount.update_forward_refs()
BasePlace.update_forward_refs()
BaseRepostsInfo.update_forward_refs()
BaseSticker.update_forward_refs()
BoardTopic.update_forward_refs()
CommentThread.update_forward_refs()
DocsDoc.update_forward_refs()
DocsDocPreview.update_forward_refs()
DocsDocPreviewAudioMsg.update_forward_refs()
DocsDocPreviewGraffiti.update_forward_refs()
DocsDocPreviewPhoto.update_forward_refs()
DocsDocPreviewVideo.update_forward_refs()
EventsEventAttach.update_forward_refs()
FriendsRequestsMutual.update_forward_refs()
GiftsLayout.update_forward_refs()
GroupsAddressTimetable.update_forward_refs()
GroupsAddressTimetableDay.update_forward_refs()
GroupsBanInfo.update_forward_refs()
GroupsGroup.update_forward_refs()
GroupsGroupAttach.update_forward_refs()
GroupsLongPollEvents.update_forward_refs()
LinkTargetObject.update_forward_refs()
MarketCurrency.update_forward_refs()
MarketMarketAlbum.update_forward_refs()
MarketMarketCategory.update_forward_refs()
MarketMarketCategoryNested.update_forward_refs()
MarketMarketItem.update_forward_refs()
MarketPrice.update_forward_refs()
MarketSection.update_forward_refs()
MediaRestriction.update_forward_refs()
MessagesAudioMessage.update_forward_refs()
MessagesChatPushSettings.update_forward_refs()
MessagesConversation.update_forward_refs()
MessagesConversationPeer.update_forward_refs()
MessagesForeignMessage.update_forward_refs()
MessagesGraffiti.update_forward_refs()
MessagesHistoryMessageAttachment.update_forward_refs()
MessagesKeyboard.update_forward_refs()
MessagesKeyboardButtonAction.update_forward_refs()
MessagesMessage.update_forward_refs()
MessagesMessageAction.update_forward_refs()
MessagesMessageActionPhoto.update_forward_refs()
MessagesMessageRequestData.update_forward_refs()
MessagesOutReadBy.update_forward_refs()
NewsfeedItemDigestFooterButton.update_forward_refs()
NotificationsFeedback.update_forward_refs()
NotificationsReply.update_forward_refs()
NotificationsSendMessageError.update_forward_refs()
PagesWikipageFull.update_forward_refs()
PhotosPhoto.update_forward_refs()
PhotosPhotoAlbum.update_forward_refs()
PollsBackground.update_forward_refs()
PollsPoll.update_forward_refs()
PollsVotersUsers.update_forward_refs()
StatsActivity.update_forward_refs()
StatsReach.update_forward_refs()
StatsViews.update_forward_refs()
StoriesClickableStickers.update_forward_refs()
StoriesPromoBlock.update_forward_refs()
StoriesReplies.update_forward_refs()
StoriesStory.update_forward_refs()
StoriesStoryLink.update_forward_refs()
StoriesStoryStatsStat.update_forward_refs()
UsersPersonal.update_forward_refs()
UsersUserConnections.update_forward_refs()
UsersUserMin.update_forward_refs()
VideoRestrictionButton.update_forward_refs()
WallAppPost.update_forward_refs()
WallAttachedNote.update_forward_refs()
WallGeo.update_forward_refs()
WallGraffiti.update_forward_refs()
WallPostCopyright.update_forward_refs()
WallPostSource.update_forward_refs()
WallPostedPhoto.update_forward_refs()
WallViews.update_forward_refs()
WallWallComment.update_forward_refs()
WallWallCommentDonut.update_forward_refs()
WallWallCommentDonutPlaceholder.update_forward_refs()
WallWallpost.update_forward_refs()
WallWallpostCommentsDonut.update_forward_refs()
WallWallpostCommentsDonutPlaceholder.update_forward_refs()
WallWallpostDonutPlaceholder.update_forward_refs()
WidgetsCommentMedia.update_forward_refs()
WidgetsCommentReplies.update_forward_refs()
WidgetsWidgetLikes.update_forward_refs()
AccountAccountCounters.update_forward_refs()
AccountInfo.update_forward_refs()
AccountOffer.update_forward_refs()
AccountPushConversationsItem.update_forward_refs()
AccountPushSettings.update_forward_refs()
AdsAccesses.update_forward_refs()
AdsAccount.update_forward_refs()
AdsAd.update_forward_refs()
AdsAdLayout.update_forward_refs()
AdsCampaign.update_forward_refs()
AdsCategory.update_forward_refs()
AdsClient.update_forward_refs()
AdsCriteria.update_forward_refs()
AdsDemoStats.update_forward_refs()
AdsFloodStats.update_forward_refs()
AdsLinkStatus.update_forward_refs()
AdsLookalikeRequest.update_forward_refs()
AdsLookalikeRequestSaveAudienceLevel.update_forward_refs()
AdsMusician.update_forward_refs()
AdsParagraphs.update_forward_refs()
AdsPromotedPostReach.update_forward_refs()
AdsRejectReason.update_forward_refs()
AdsRules.update_forward_refs()
AdsStats.update_forward_refs()
AdsStatsAge.update_forward_refs()
AdsStatsCities.update_forward_refs()
AdsStatsSex.update_forward_refs()
AdsStatsSexAge.update_forward_refs()
AdsTargStats.update_forward_refs()
AdsTargSuggestions.update_forward_refs()
AdsTargSuggestionsCities.update_forward_refs()
AdsTargSuggestionsRegions.update_forward_refs()
AdsTargSuggestionsSchools.update_forward_refs()
AdsTargetGroup.update_forward_refs()
AdsUpdateOfficeUsersResult.update_forward_refs()
AdsUserSpecification.update_forward_refs()
AdsUserSpecificationCutted.update_forward_refs()
AdsUsers.update_forward_refs()
AdswebGetAdCategoriesResponseCategoriesCategory.update_forward_refs()
AdswebGetAdUnitsResponseAdUnitsAdUnit.update_forward_refs()
AdswebGetFraudHistoryResponseEntriesEntry.update_forward_refs()
AdswebGetSitesResponseSitesSite.update_forward_refs()
AdswebGetStatisticsResponseItemsItem.update_forward_refs()
AppWidgetsPhoto.update_forward_refs()
AppWidgetsPhotos.update_forward_refs()
AppsLeaderboard.update_forward_refs()
AppsScope.update_forward_refs()
BaseCropPhoto.update_forward_refs()
BaseGradientPoint.update_forward_refs()
BaseImage.update_forward_refs()
BaseMessageError.update_forward_refs()
BaseObject.update_forward_refs()
BaseObjectWithName.update_forward_refs()
BaseRequestParam.update_forward_refs()
BaseStickerAnimation.update_forward_refs()
BaseUploadServer.update_forward_refs()
BaseUserId.update_forward_refs()
BoardTopicComment.update_forward_refs()
BoardTopicPoll.update_forward_refs()
CallbackBoardPostDelete.update_forward_refs()
CallbackConfirmationMessage.update_forward_refs()
CallbackDonutMoneyWithdraw.update_forward_refs()
CallbackDonutMoneyWithdrawError.update_forward_refs()
CallbackDonutSubscriptionCancelled.update_forward_refs()
CallbackDonutSubscriptionCreate.update_forward_refs()
CallbackDonutSubscriptionExpired.update_forward_refs()
CallbackDonutSubscriptionPriceChanged.update_forward_refs()
CallbackDonutSubscriptionProlonged.update_forward_refs()
CallbackGroupChangePhoto.update_forward_refs()
CallbackGroupChangeSettings.update_forward_refs()
CallbackGroupJoin.update_forward_refs()
CallbackGroupLeave.update_forward_refs()
CallbackGroupOfficersEdit.update_forward_refs()
CallbackGroupSettingsChanges.update_forward_refs()
CallbackLikeAddRemove.update_forward_refs()
CallbackMarketComment.update_forward_refs()
CallbackMarketCommentDelete.update_forward_refs()
CallbackMessageAllow.update_forward_refs()
CallbackMessageBase.update_forward_refs()
CallbackMessageDeny.update_forward_refs()
CallbackPhotoComment.update_forward_refs()
CallbackPhotoCommentDelete.update_forward_refs()
CallbackPollVoteNew.update_forward_refs()
CallbackQrScan.update_forward_refs()
CallbackUserBlock.update_forward_refs()
CallbackUserUnblock.update_forward_refs()
CallbackVideoComment.update_forward_refs()
CallbackVideoCommentDelete.update_forward_refs()
CallbackWallCommentDelete.update_forward_refs()
DatabaseFaculty.update_forward_refs()
DatabaseRegion.update_forward_refs()
DatabaseSchool.update_forward_refs()
DatabaseStation.update_forward_refs()
DatabaseUniversity.update_forward_refs()
DocsDocPreviewPhotoSizes.update_forward_refs()
DocsDocTypes.update_forward_refs()
DocsDocUploadResponse.update_forward_refs()
DonutDonatorSubscriptionInfo.update_forward_refs()
FaveBookmark.update_forward_refs()
FavePage.update_forward_refs()
FaveTag.update_forward_refs()
FriendsFriendStatus.update_forward_refs()
FriendsFriendsList.update_forward_refs()
FriendsMutualFriend.update_forward_refs()
FriendsRequests.update_forward_refs()
FriendsRequestsXtrMessage.update_forward_refs()
GiftsGift.update_forward_refs()
GroupsAddress.update_forward_refs()
GroupsAddressesInfo.update_forward_refs()
GroupsBannedItem.update_forward_refs()
GroupsCallbackServer.update_forward_refs()
GroupsCallbackSettings.update_forward_refs()
GroupsContactsItem.update_forward_refs()
GroupsCountersGroup.update_forward_refs()
GroupsCover.update_forward_refs()
GroupsGroupBanInfo.update_forward_refs()
GroupsGroupCategory.update_forward_refs()
GroupsGroupCategoryFull.update_forward_refs()
GroupsGroupCategoryType.update_forward_refs()
GroupsGroupLink.update_forward_refs()
GroupsGroupPublicCategoryList.update_forward_refs()
GroupsGroupTag.update_forward_refs()
GroupsGroupXtrInvitedBy.update_forward_refs()
GroupsGroupsArray.update_forward_refs()
GroupsLinksItem.update_forward_refs()
GroupsLiveCovers.update_forward_refs()
GroupsLongPollServer.update_forward_refs()
GroupsLongPollSettings.update_forward_refs()
GroupsMarketInfo.update_forward_refs()
GroupsMemberRole.update_forward_refs()
GroupsMemberStatus.update_forward_refs()
GroupsMemberStatusFull.update_forward_refs()
GroupsOnlineStatus.update_forward_refs()
GroupsOwnerXtrBanInfo.update_forward_refs()
GroupsProfileItem.update_forward_refs()
GroupsSettingsTwitter.update_forward_refs()
GroupsSubjectItem.update_forward_refs()
GroupsTokenPermissionSetting.update_forward_refs()
MarketMarketCategoryOld.update_forward_refs()
MarketMarketCategoryTree.update_forward_refs()
MarketOrder.update_forward_refs()
MarketOrderItem.update_forward_refs()
MessagesChat.update_forward_refs()
MessagesChatFull.update_forward_refs()
MessagesChatPreview.update_forward_refs()
MessagesChatRestrictions.update_forward_refs()
MessagesConversationMember.update_forward_refs()
MessagesConversationWithMessage.update_forward_refs()
MessagesForward.update_forward_refs()
MessagesHistoryAttachment.update_forward_refs()
MessagesKeyboardButton.update_forward_refs()
MessagesLastActivity.update_forward_refs()
MessagesConversationChatSettings.update_forward_refs()
MessagesLongpollMessages.update_forward_refs()
MessagesLongpollParams.update_forward_refs()
MessagesMessageAttachment.update_forward_refs()
MessagesMessagesArray.update_forward_refs()
MessagesPinnedMessage.update_forward_refs()
NewsfeedEventActivity.update_forward_refs()
NewsfeedItemAudioAudio.update_forward_refs()
NewsfeedItemBase.update_forward_refs()
NewsfeedItemDigestFooter.update_forward_refs()
NewsfeedItemDigestHeader.update_forward_refs()
NewsfeedItemFriendFriends.update_forward_refs()
NewsfeedItemHolidayRecommendationsBlockHeader.update_forward_refs()
NewsfeedItemPhotoPhotos.update_forward_refs()
NewsfeedItemPhotoTagPhotoTags.update_forward_refs()
NewsfeedItemPromoButtonAction.update_forward_refs()
NewsfeedItemPromoButtonImage.update_forward_refs()
NewsfeedItemVideoVideo.update_forward_refs()
NewsfeedItemWallpostFeedback.update_forward_refs()
NewsfeedItemWallpostFeedbackAnswer.update_forward_refs()
NewsfeedList.update_forward_refs()
NotesNote.update_forward_refs()
NotesNoteComment.update_forward_refs()
NotificationsNotification.update_forward_refs()
NotificationsNotificationsComment.update_forward_refs()
NotificationsSendMessageItem.update_forward_refs()
OauthError.update_forward_refs()
OrdersAmount.update_forward_refs()
OrdersAmountItem.update_forward_refs()
OrdersOrder.update_forward_refs()
OrdersSubscription.update_forward_refs()
OwnerState.update_forward_refs()
PagesWikipage.update_forward_refs()
PagesWikipageHistory.update_forward_refs()
PhotosCommentXtrPid.update_forward_refs()
PhotosImage.update_forward_refs()
PhotosMarketAlbumUploadResponse.update_forward_refs()
PhotosMarketUploadResponse.update_forward_refs()
PhotosMessageUploadResponse.update_forward_refs()
PhotosOwnerUploadResponse.update_forward_refs()
PhotosPhotoAlbumFull.update_forward_refs()
PhotosPhotoFull.update_forward_refs()
PhotosPhotoFullXtrRealOffset.update_forward_refs()
PhotosPhotoSizes.update_forward_refs()
PhotosPhotoTag.update_forward_refs()
PhotosPhotoUpload.update_forward_refs()
PhotosPhotoUploadResponse.update_forward_refs()
PhotosPhotoXtrRealOffset.update_forward_refs()
PhotosPhotoXtrTagInfo.update_forward_refs()
PhotosTagsSuggestionItem.update_forward_refs()
PhotosTagsSuggestionItemButton.update_forward_refs()
PhotosWallUploadResponse.update_forward_refs()
PollsAnswer.update_forward_refs()
PollsFriend.update_forward_refs()
PollsVoters.update_forward_refs()
PrettyCardsPrettyCard.update_forward_refs()
SearchHint.update_forward_refs()
SecureLevel.update_forward_refs()
SecureSmsNotification.update_forward_refs()
SecureTokenChecked.update_forward_refs()
SecureTransaction.update_forward_refs()
StatsCity.update_forward_refs()
StatsCountry.update_forward_refs()
StatsPeriod.update_forward_refs()
StatsSexAge.update_forward_refs()
StatsWallpostStat.update_forward_refs()
StatusStatus.update_forward_refs()
StorageValue.update_forward_refs()
StoriesClickableArea.update_forward_refs()
StoriesClickableSticker.update_forward_refs()
StoriesFeedItem.update_forward_refs()
StoriesStatLine.update_forward_refs()
StoriesStoryStats.update_forward_refs()
StoriesViewersItem.update_forward_refs()
UsersCareer.update_forward_refs()
UsersExports.update_forward_refs()
UsersLastSeen.update_forward_refs()
UsersMilitary.update_forward_refs()
UsersOccupation.update_forward_refs()
UsersOnlineInfo.update_forward_refs()
UsersRelative.update_forward_refs()
UsersSchool.update_forward_refs()
UsersUniversity.update_forward_refs()
UsersUserCounters.update_forward_refs()
UsersUserSettingsXtr.update_forward_refs()
UsersUsersArray.update_forward_refs()
UtilsDomainResolved.update_forward_refs()
UtilsLastShortenedLink.update_forward_refs()
UtilsLinkChecked.update_forward_refs()
UtilsLinkStats.update_forward_refs()
UtilsLinkStatsExtended.update_forward_refs()
UtilsShortLink.update_forward_refs()
UtilsStats.update_forward_refs()
UtilsStatsCity.update_forward_refs()
UtilsStatsCountry.update_forward_refs()
UtilsStatsExtended.update_forward_refs()
UtilsStatsSexAge.update_forward_refs()
VideoLiveInfo.update_forward_refs()
VideoLiveSettings.update_forward_refs()
VideoSaveResult.update_forward_refs()
VideoVideoAlbumFull.update_forward_refs()
VideoVideoFiles.update_forward_refs()
WallCarouselBase.update_forward_refs()
WallCommentAttachment.update_forward_refs()
WallWallpostAttachment.update_forward_refs()
WallWallpostDonut.update_forward_refs()
WallWallpostToId.update_forward_refs()
WidgetsCommentRepliesItem.update_forward_refs()
WidgetsWidgetComment.update_forward_refs()
WidgetsWidgetPage.update_forward_refs()
UsersUser.update_forward_refs()
UsersUserFull.update_forward_refs()
UsersUserXtrType.update_forward_refs()
AccountUserSettings.update_forward_refs()
AdsTargSettings.update_forward_refs()
AppsApp.update_forward_refs()
DatabaseCity.update_forward_refs()
FriendsFriendExtendedStatus.update_forward_refs()
FriendsUserXtrLists.update_forward_refs()
FriendsUserXtrPhone.update_forward_refs()
GroupsBannedItem.update_forward_refs()
GroupsGroupFull.update_forward_refs()
GroupsUserXtrRole.update_forward_refs()
MarketMarketCategory.update_forward_refs()
MarketMarketItemFull.update_forward_refs()
MessagesUserXtrInvitedBy.update_forward_refs()
NewsfeedItemAudio.update_forward_refs()
NewsfeedItemDigest.update_forward_refs()
NewsfeedItemFriend.update_forward_refs()
NewsfeedItemPhoto.update_forward_refs()
NewsfeedItemPhotoTag.update_forward_refs()
NewsfeedItemPromoButton.update_forward_refs()
NewsfeedItemTopic.update_forward_refs()
NewsfeedItemVideo.update_forward_refs()
NewsfeedItemWallpost.update_forward_refs()
NewsfeedListFull.update_forward_refs()
NewsfeedNewsfeedItem.update_forward_refs()
NewsfeedNewsfeedPhoto.update_forward_refs()
NotificationsNotificationParent.update_forward_refs()
PhotosPhotoFalseable.update_forward_refs()
UsersSubscriptionsItem.update_forward_refs()
UsersUserXtrCounters.update_forward_refs()
VideoVideo.update_forward_refs()
VideoVideoFull.update_forward_refs()
VideoVideoImage.update_forward_refs()
WallWallpostFull.update_forward_refs()
