import json
from common.do_mysql import DoMySql
import requests
from common.deal_with_data import count_time

a = [
    {
        "name_abbr": "AF",
        "country": "阿富汗",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Afghanistan"
    },
    {
        "name_abbr": "AL",
        "country": "阿尔巴尼亚",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Albania"
    },
    {
        "name_abbr": "DZ",
        "country": "阿尔及利亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Algeria"
    },
    {
        "name_abbr": "AD",
        "country": "安道尔",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Andorra"
    },
    {
        "name_abbr": "AO",
        "country": "安哥拉",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Angola"
    },
    {
        "name_abbr": "AI",
        "country": "安圭拉",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Anguilla"
    },
    {
        "name_abbr": "AG",
        "country": "安提瓜和巴布达岛",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Antigua"
    },
    {
        "name_abbr": "AE",
        "country": "阿联酋",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Arab"
    },
    {
        "name_abbr": "AR",
        "country": "阿根廷",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Argentina"
    },
    {
        "name_abbr": "AM",
        "country": "亚美尼亚",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Armenia"
    },
    {
        "name_abbr": "AW",
        "country": "阿鲁巴",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Aruba"
    },
    {
        "name_abbr": "AU",
        "country": "澳大利亚",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Australia"
    },
    {
        "name_abbr": "AT",
        "country": "奥地利",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Austria"
    },
    {
        "name_abbr": "AT",
        "country": "奥地利",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Austria"
    },
    {
        "name_abbr": "AZ",
        "country": "阿塞拜疆",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Azerbaijan"
    },
    {
        "name_abbr": "BS",
        "country": "巴哈马",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Bahamas"
    },
    {
        "name_abbr": "BH",
        "country": "巴林",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Bahrain"
    },
    {
        "name_abbr": "BD",
        "country": "孟加拉国",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Bangladesh"
    },
    {
        "name_abbr": "BB",
        "country": "巴巴多斯",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Barbados"
    },
    {
        "name_abbr": "BY",
        "country": "白俄罗斯",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Belarus"
    },
    {
        "name_abbr": "BE",
        "country": "比利时",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Belgium"
    },
    {
        "name_abbr": "BZ",
        "country": "伯利兹",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Belize"
    },
    {
        "name_abbr": "BJ",
        "country": "贝宁",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Benin"
    },
    {
        "name_abbr": "BM",
        "country": "百慕大群岛",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Bermuda"
    },
    {
        "name_abbr": "BT",
        "country": "不丹",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Bhutan"
    },
    {
        "name_abbr": "BO",
        "country": "玻利维亚",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Bolivia"
    },
    {
        "name_abbr": "BIH",
        "country": "Bosnia和Herzegovina",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Bosnia"
    },
    {
        "name_abbr": "BW",
        "country": "博茨瓦纳",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Botswana"
    },
    {
        "name_abbr": "BR",
        "country": "巴西",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Brazil"
    },
    {
        "name_abbr": "BN",
        "country": "文莱",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Brunei"
    },
    {
        "name_abbr": "BG",
        "country": "保加利亚",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Bulgaria"
    },
    {
        "name_abbr": "BF",
        "country": "布基纳法索",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Burkina"
    },
    {
        "name_abbr": "BI",
        "country": "布隆迪",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Burundi"
    },
    {
        "name_abbr": "KH",
        "country": "柬埔寨",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Cambodia"
    },
    {
        "name_abbr": "CM",
        "country": "喀麦隆",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Cameroon"
    },
    {
        "name_abbr": "CA",
        "country": "加拿大",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Canada"
    },
    {
        "name_abbr": "CV",
        "country": "佛得角",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Cape"
    },
    {
        "name_abbr": "KY",
        "country": "开曼群岛",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Cayman"
    },
    {
        "name_abbr": "CF",
        "country": "中非",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Central"
    },
    {
        "name_abbr": "TD",
        "country": "乍得",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Chad"
    },
    {
        "name_abbr": "CL",
        "country": "智利",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Chile"
    },
    {
        "name_abbr": "HK",
        "country": "中国香港",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "China,"
    },
    {
        "name_abbr": "CN",
        "country": "中国大陆",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "China,"
    },
    {
        "name_abbr": "CO",
        "country": "哥伦比亚",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Colombia"
    },
    {
        "name_abbr": "KM",
        "country": "科摩罗",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Comoros"
    },
    {
        "name_abbr": "CG",
        "country": "刚果（布）",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Congo"
    },
    {
        "name_abbr": "CD",
        "country": "刚果（金）",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Congo"
    },
    {
        "name_abbr": "CK",
        "country": "库克群岛",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Cook"
    },
    {
        "name_abbr": "CR",
        "country": "哥斯达黎加",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Costa"
    },
    {
        "name_abbr": "HR",
        "country": "克罗地亚",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Croatia"
    },
    {
        "name_abbr": "CU",
        "country": "古巴",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Cuba"
    },
    {
        "name_abbr": "CY",
        "country": "塞浦路斯",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Cyprus"
    },
    {
        "name_abbr": "CZ",
        "country": "捷克",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Czech"
    },
    {
        "name_abbr": "CS",
        "country": "捷克斯洛伐克",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Czechoslovakia"
    },
    {
        "name_abbr": "DK",
        "country": "丹麦",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Denmark"
    },
    {
        "name_abbr": "DJ",
        "country": "吉布提",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Djibouti"
    },
    {
        "name_abbr": "DM",
        "country": "多米尼加",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Dominica"
    },
    {
        "name_abbr": "DO",
        "country": "多明尼加",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Dominican"
    },
    {
        "name_abbr": "EC",
        "country": "厄瓜多尔",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Ecuador"
    },
    {
        "name_abbr": "EG",
        "country": "埃及",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Egypt"
    },
    {
        "name_abbr": "SV",
        "country": "萨尔瓦多",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "El"
    },
    {
        "name_abbr": "GQ",
        "country": "赤道几内亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Equatorial"
    },
    {
        "name_abbr": "ER",
        "country": "厄立特里亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Eritrea"
    },
    {
        "name_abbr": "EE",
        "country": "爱沙尼亚",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Estonia"
    },
    {
        "name_abbr": "ET",
        "country": "埃塞俄比亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Ethiopia"
    },
    {
        "name_abbr": "FJ",
        "country": "斐济",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Fiji"
    },
    {
        "name_abbr": "FI",
        "country": "芬兰",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Finland"
    },
    {
        "name_abbr": "FR",
        "country": "法国",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "France"
    },
    {
        "name_abbr": "GF",
        "country": "法属圭亚那",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "French"
    },
    {
        "name_abbr": "PF",
        "country": "法属波利尼西亚",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "French"
    },
    {
        "name_abbr": "GA",
        "country": "加蓬",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Gabon"
    },
    {
        "name_abbr": "GM",
        "country": "冈比亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Gambia"
    },
    {
        "name_abbr": "GE",
        "country": "格鲁吉亚",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Georgia,"
    },
    {
        "name_abbr": "DD",
        "country": "德国",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "German"
    },
    {
        "name_abbr": "GH",
        "country": "加纳",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Ghana"
    },
    {
        "name_abbr": "GI",
        "country": "直布罗陀",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Gibraltar"
    },
    {
        "name_abbr": "GR",
        "country": "希腊",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Greece"
    },
    {
        "name_abbr": "GD",
        "country": "格林纳达",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Grenada"
    },
    {
        "name_abbr": "GT",
        "country": "危地马拉",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Guatemala"
    },
    {
        "name_abbr": "GN",
        "country": "几内亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Guinea"
    },
    {
        "name_abbr": "GW",
        "country": "几内亚比绍",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Guinea-Bissau"
    },
    {
        "name_abbr": "GY",
        "country": "圭亚那",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Guyana"
    },
    {
        "name_abbr": "HT",
        "country": "海地",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Haiti"
    },
    {
        "name_abbr": "HN",
        "country": "洪都拉斯",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Honduras"
    },
    {
        "name_abbr": "HU",
        "country": "匈牙利",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Hungary"
    },
    {
        "name_abbr": "IS",
        "country": "冰岛",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Iceland"
    },
    {
        "name_abbr": "IN",
        "country": "印度",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "India"
    },
    {
        "name_abbr": "ID",
        "country": "印度尼西亚",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Indonesia"
    },
    {
        "name_abbr": "IR",
        "country": "伊朗",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Iran"
    },
    {
        "name_abbr": "IQ",
        "country": "伊拉克",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Iraq"
    },
    {
        "name_abbr": "IE",
        "country": "爱尔兰",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Ireland"
    },
    {
        "name_abbr": "IM",
        "country": "马恩岛",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Isle"
    },
    {
        "name_abbr": "IL",
        "country": "以色列",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Israel"
    },
    {
        "name_abbr": "IT",
        "country": "意大利",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Italy"
    },
    {
        "name_abbr": "CI",
        "country": "科特迪瓦",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Ivory"
    },
    {
        "name_abbr": "JM",
        "country": "牙买加",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Jamaica"
    },
    {
        "name_abbr": "JP",
        "country": "日本",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Japan"
    },
    {
        "name_abbr": "JE",
        "country": "泽西",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Jersey"
    },
    {
        "name_abbr": "JO",
        "country": "乔丹",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Jordan"
    },
    {
        "name_abbr": "KZ",
        "country": "哈萨克斯坦",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Kazakhstan"
    },
    {
        "name_abbr": "KE",
        "country": "肯尼亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Kenya"
    },
    {
        "name_abbr": "KI",
        "country": "基里巴斯",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Kiribati"
    },
    {
        "name_abbr": "KW",
        "country": "科威特",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Kuwait"
    },
    {
        "name_abbr": "KG",
        "country": "吉尔吉斯斯坦",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Kyrgyzstan"
    },
    {
        "name_abbr": "LA",
        "country": "老挝",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Laos"
    },
    {
        "name_abbr": "LV",
        "country": "拉脱维亚",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Latvia"
    },
    {
        "name_abbr": "LB",
        "country": "黎巴嫩",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Lebanon"
    },
    {
        "name_abbr": "LS",
        "country": "莱索托",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Lesotho"
    },
    {
        "name_abbr": "LR",
        "country": "利比里亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Liberia"
    },
    {
        "name_abbr": "LY",
        "country": "利比亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Libya"
    },
    {
        "name_abbr": "LI",
        "country": "列支敦士登",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Liechtenstein"
    },
    {
        "name_abbr": "LT",
        "country": "立陶宛",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Lithuania"
    },
    {
        "name_abbr": "LU",
        "country": "卢森堡",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Luxembourg"
    },
    {
        "name_abbr": "MO",
        "country": "澳门",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Macau"
    },
    {
        "name_abbr": "MG",
        "country": "马达加斯加",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Madagascar"
    },
    {
        "name_abbr": "MW",
        "country": "马拉维",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Malawi"
    },
    {
        "name_abbr": "MY",
        "country": "马来西亚",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Malaysia"
    },
    {
        "name_abbr": "MV",
        "country": "马尔代夫",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Maldives"
    },
    {
        "name_abbr": "ML",
        "country": "马里",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Mali"
    },
    {
        "name_abbr": "MT",
        "country": "马耳他",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Malta"
    },
    {
        "name_abbr": "MH",
        "country": "马绍尔群岛",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Marshall"
    },
    {
        "name_abbr": "MQ",
        "country": "马提尼克",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Martinique"
    },
    {
        "name_abbr": "MR",
        "country": "毛里塔尼亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Mauritania"
    },
    {
        "name_abbr": "MU",
        "country": "毛里求斯",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Mauritius"
    },
    {
        "name_abbr": "MX",
        "country": "墨西哥",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Mexico"
    },
    {
        "name_abbr": "MD",
        "country": "摩尔多瓦",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Moldova"
    },
    {
        "name_abbr": "MC",
        "country": "摩纳哥",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Monaco"
    },
    {
        "name_abbr": "MN",
        "country": "蒙古",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Mongolia"
    },
    {
        "name_abbr": "ME",
        "country": "黑山",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Montenegro"
    },
    {
        "name_abbr": "MA",
        "country": "摩洛哥",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Morocco"
    },
    {
        "name_abbr": "MZ",
        "country": "莫桑比克",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Mozambique"
    },
    {
        "name_abbr": "MM",
        "country": "缅甸",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Myanmar"
    },
    {
        "name_abbr": "NA",
        "country": "纳米比亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Namibia"
    },
    {
        "name_abbr": "NR",
        "country": "瑙鲁",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Nauru"
    },
    {
        "name_abbr": "NP",
        "country": "尼泊尔",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Nepal"
    },
    {
        "name_abbr": "NL",
        "country": "荷兰",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Netherlands"
    },
    {
        "name_abbr": "AN",
        "country": "荷属安的列斯群岛",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Netherlands"
    },
    {
        "name_abbr": "NC",
        "country": "新喀里多尼亚",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "New"
    },
    {
        "name_abbr": "PG",
        "country": "新几内亚",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "New"
    },
    {
        "name_abbr": "NZ",
        "country": "新西兰",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "New"
    },
    {
        "name_abbr": "NI",
        "country": "尼加拉瓜",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Nicaragua"
    },
    {
        "name_abbr": "NE",
        "country": "尼日尔",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Niger"
    },
    {
        "name_abbr": "NG",
        "country": "尼日利亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Nigeria"
    },
    {
        "name_abbr": "KP",
        "country": "朝鲜",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "North"
    },
    {
        "name_abbr": "MP",
        "country": "北马里亚纳群岛",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Northern"
    },
    {
        "name_abbr": "NO",
        "country": "挪威",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Norway"
    },
    {
        "name_abbr": "OM",
        "country": "阿曼",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Oman"
    },
    {
        "name_abbr": "PK",
        "country": "巴基斯坦",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Pakistan"
    },
    {
        "name_abbr": "PW",
        "country": "帕劳",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Palau"
    },
    {
        "name_abbr": "PA",
        "country": "巴拿马",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Panama"
    },
    {
        "name_abbr": "PNG",
        "country": "巴布亚新几内亚",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Papua"
    },
    {
        "name_abbr": "PY",
        "country": "巴拉圭",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Paraguay"
    },
    {
        "name_abbr": "PE",
        "country": "秘鲁",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Peru"
    },
    {
        "name_abbr": "PH",
        "country": "菲律宾",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Philippines"
    },
    {
        "name_abbr": "PL",
        "country": "波兰",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Poland"
    },
    {
        "name_abbr": "PT",
        "country": "葡萄牙",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Portugal"
    },
    {
        "name_abbr": "QA",
        "country": "卡塔尔",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Qatar"
    },
    {
        "name_abbr": "RH",
        "country": "罗得西亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Rhodesia"
    },
    {
        "name_abbr": "RO",
        "country": "罗马尼亚",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Romania"
    },
    {
        "name_abbr": "RU",
        "country": "俄罗斯",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Russian"
    },
    {
        "name_abbr": "RW",
        "country": "卢旺达",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Rwanda"
    },
    {
        "name_abbr": "WS",
        "country": "萨摩亚",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Samoa"
    },
    {
        "name_abbr": "SM",
        "country": "圣马力诺",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "San"
    },
    {
        "name_abbr": "ST",
        "country": "圣多美和普林西比",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Sao"
    },
    {
        "name_abbr": "SA",
        "country": "沙特阿拉伯",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Saudi"
    },
    {
        "name_abbr": "SN",
        "country": "塞内加尔",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Senegal"
    },
    {
        "name_abbr": "RS",
        "country": "塞尔维亚",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Serbia"
    },
    {
        "name_abbr": "SC",
        "country": "塞舌尔",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Seychelles"
    },
    {
        "name_abbr": "SL",
        "country": "塞拉利昂",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Sierra"
    },
    {
        "name_abbr": "SG",
        "country": "新加坡",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Singapore"
    },
    {
        "name_abbr": "SK",
        "country": "斯洛伐克",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Slovakia"
    },
    {
        "name_abbr": "SI",
        "country": "斯洛文尼亚",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Slovenia"
    },
    {
        "name_abbr": "SB",
        "country": "所罗门群岛",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Solomon"
    },
    {
        "name_abbr": "SO",
        "country": "索马里",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Somalia"
    },
    {
        "name_abbr": "ZA",
        "country": "南非",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "South"
    },
    {
        "name_abbr": "KR",
        "country": "韩国",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "South"
    },
    {
        "name_abbr": "ES",
        "country": "西班牙",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Spain"
    },
    {
        "name_abbr": "LK",
        "country": "斯里兰卡",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Sri"
    },
    {
        "name_abbr": "LC",
        "country": "圣露西亚",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "St."
    },
    {
        "name_abbr": "VC",
        "country": "圣文森特和格林纳丁斯",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "St."
    },
    {
        "name_abbr": "SD",
        "country": "苏丹",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Sudan"
    },
    {
        "name_abbr": "SR",
        "country": "苏里南",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Suriname"
    },
    {
        "name_abbr": "SZ",
        "country": "斯威士兰",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Swaziland"
    },
    {
        "name_abbr": "SE",
        "country": "瑞典",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Sweden"
    },
    {
        "name_abbr": "CH",
        "country": "瑞士",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Switzerland"
    },
    {
        "name_abbr": "SY",
        "country": "叙利亚",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Syria"
    },
    {
        "name_abbr": "TW",
        "country": "中国，台湾",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Taiwan"
    },
    {
        "name_abbr": "CN",
        "country": "中国",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "China"
    },
    {
        "name_abbr": "TJ",
        "country": "塔吉克斯坦",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Tajikistan"
    },
    {
        "name_abbr": "TZ",
        "country": "坦桑尼亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Tanzania"
    },
    {
        "name_abbr": "TH",
        "country": "泰国",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Thailand"
    },
    {
        "name_abbr": "TL",
        "country": "东帝汶",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Timor-Leste"
    },
    {
        "name_abbr": "TG",
        "country": "多哥",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Togo"
    },
    {
        "name_abbr": "TO",
        "country": "汤加",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Tonga"
    },
    {
        "name_abbr": "TT",
        "country": "特立尼达和多巴哥",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Trinidad"
    },
    {
        "name_abbr": "TN",
        "country": "突尼斯",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Tunisia"
    },
    {
        "name_abbr": "TR",
        "country": "土耳其",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Turkey"
    },
    {
        "name_abbr": "TM",
        "country": "土库曼斯坦",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Turkmenistan"
    },
    {
        "name_abbr": "TV",
        "country": "图瓦卢",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Tuvalu"
    },
    {
        "name_abbr": "SU",
        "country": "苏联",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "USSR"
    },
    {
        "name_abbr": "UG",
        "country": "乌干达",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Uganda"
    },
    {
        "name_abbr": "UA",
        "country": "乌克兰",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Ukraine"
    },
    {
        "name_abbr": "GB",
        "country": "英国",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "United"
    },
    {
        "name_abbr": "US",
        "country": "美国",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "United"
    },
    {
        "name_abbr": "UY",
        "country": "乌拉圭",
        "continent": "南美洲",
        "continent_abbr": "SA",
        "name_en": "Uruguay"
    },
    {
        "name_abbr": "UZ",
        "country": "乌兹别克斯坦",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Uzbekistan"
    },
    {
        "name_abbr": "VU",
        "country": "瓦努阿图",
        "continent": "大洋洲",
        "continent_abbr": "OA",
        "name_en": "Vanuatu"
    },
    {
        "name_abbr": "VA",
        "country": "梵蒂冈",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Vatican"
    },
    {
        "name_abbr": "VE",
        "country": "委内瑞拉",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Venezuela"
    },
    {
        "name_abbr": "VN",
        "country": "越南",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Viet"
    },
    {
        "name_abbr": "VG",
        "country": "(英属)维尔京群岛",
        "continent": "北美洲",
        "continent_abbr": "NA",
        "name_en": "Virgin (British) Islands"
    },
    {
        "name_abbr": "EH",
        "country": "西撒哈拉",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Western"
    },
    {
        "name_abbr": "YE",
        "country": "也门",
        "continent": "亚洲",
        "continent_abbr": "AS",
        "name_en": "Yemen"
    },
    {
        "name_abbr": "YU",
        "country": "南斯拉夫",
        "continent": "欧洲",
        "continent_abbr": "EU",
        "name_en": "Yugoslavia"
    },
    {
        "name_abbr": "ZM",
        "country": "赞比亚",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Zambia"
    },
    {
        "name_abbr": "ZW",
        "country": "津巴布韦",
        "continent": "非洲",
        "continent_abbr": "AF",
        "name_en": "Zimbabwe"
    }
]
coun = []
for  i in a:
    coun.append(i['country'])
print(coun)
