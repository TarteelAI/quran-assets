import json
import os

dirname = os.path.dirname(__file__)
metadata_dir = os.path.join(dirname, '../metadata')

with open(f'{metadata_dir}/ayah-count-per-surah-map.json', 'r') as f:
    data = json.load(f)

surah_keys = []
for key, val in data.items():
    surah_keys.append(f"{key}:1-{key}:{val}")

print(surah_keys)


with open(f'{metadata_dir}/page-indices-lookup.json', 'r') as f:
    data = json.load(f)

page_keys = []
for page in data:
    page_keys.append(f'{page["start"]["surah"]}:{page["start"]["ayah"]}-{page["end"]["surah"]}:{page["end"]["ayah"]}')

print(page_keys)


# Generates the following
# SURAH_KEYS = ['1:1-1:7', '2:1-2:286', '3:1-3:200', '4:1-4:176', '5:1-5:120', '6:1-6:165', '7:1-7:206', '8:1-8:75', '9:1-9:129', '10:1-10:109', '11:1-11:123', '12:1-12:111', '13:1-13:43', '14:1-14:52', '15:1-15:99', '16:1-16:128', '17:1-17:111', '18:1-18:110', '19:1-19:98', '20:1-20:135', '21:1-21:112', '22:1-22:78', '23:1-23:118', '24:1-24:64', '25:1-25:77', '26:1-26:227', '27:1-27:93', '28:1-28:88', '29:1-29:69', '30:1-30:60', '31:1-31:34', '32:1-32:30', '33:1-33:73', '34:1-34:54', '35:1-35:45', '36:1-36:83', '37:1-37:182', '38:1-38:88', '39:1-39:75', '40:1-40:85', '41:1-41:54', '42:1-42:53', '43:1-43:89', '44:1-44:59', '45:1-45:37', '46:1-46:35', '47:1-47:38', '48:1-48:29', '49:1-49:18', '50:1-50:45', '51:1-51:60', '52:1-52:49', '53:1-53:62', '54:1-54:55', '55:1-55:78', '56:1-56:96', '57:1-57:29', '58:1-58:22', '59:1-59:24', '60:1-60:13', '61:1-61:14', '62:1-62:11', '63:1-63:11', '64:1-64:18', '65:1-65:12', '66:1-66:12', '67:1-67:30', '68:1-68:52', '69:1-69:52', '70:1-70:44', '71:1-71:28', '72:1-72:28', '73:1-73:20', '74:1-74:56', '75:1-75:40', '76:1-76:31', '77:1-77:50', '78:1-78:40', '79:1-79:46', '80:1-80:42', '81:1-81:29', '82:1-82:19', '83:1-83:36', '84:1-84:25', '85:1-85:22', '86:1-86:17', '87:1-87:19', '88:1-88:26', '89:1-89:30', '90:1-90:20', '91:1-91:15', '92:1-92:21', '93:1-93:11', '94:1-94:8', '95:1-95:8', '96:1-96:19', '97:1-97:5', '98:1-98:8', '99:1-99:8', '100:1-100:11', '101:1-101:11', '102:1-102:8', '103:1-103:3', '104:1-104:9', '105:1-105:5', '106:1-106:4', '107:1-107:7', '108:1-108:3', '109:1-109:6', '110:1-110:3', '111:1-111:5', '112:1-112:4', '113:1-113:5', '114:1-114:6']
# PAGE_KEYS = ['1:1-1:7', '2:1-2:5', '2:6-2:16', '2:17-2:24', '2:25-2:29', '2:30-2:37', '2:38-2:48', '2:49-2:57', '2:58-2:61', '2:62-2:69', '2:70-2:76', '2:77-2:83', '2:84-2:88', '2:89-2:93', '2:94-2:101', '2:102-2:105', '2:106-2:112', '2:113-2:119', '2:120-2:126', '2:127-2:134', '2:135-2:141', '2:142-2:145', '2:146-2:153', '2:154-2:163', '2:164-2:169', '2:170-2:176', '2:177-2:181', '2:182-2:186', '2:187-2:190', '2:191-2:196', '2:197-2:202', '2:203-2:210', '2:211-2:215', '2:216-2:219', '2:220-2:224', '2:225-2:230', '2:231-2:233', '2:234-2:237', '2:238-2:245', '2:246-2:248', '2:249-2:252', '2:253-2:256', '2:257-2:259', '2:260-2:264', '2:265-2:269', '2:270-2:274', '2:275-2:281', '2:282-2:282', '2:283-2:286', '3:1-3:9', '3:10-3:15', '3:16-3:22', '3:23-3:29', '3:30-3:37', '3:38-3:45', '3:46-3:52', '3:53-3:61', '3:62-3:70', '3:71-3:77', '3:78-3:83', '3:84-3:91', '3:92-3:100', '3:101-3:108', '3:109-3:115', '3:116-3:121', '3:122-3:132', '3:133-3:140', '3:141-3:148', '3:149-3:153', '3:154-3:157', '3:158-3:165', '3:166-3:173', '3:174-3:180', '3:181-3:186', '3:187-3:194', '3:195-3:200', '4:1-4:6', '4:7-4:11', '4:12-4:14', '4:15-4:19', '4:20-4:23', '4:24-4:26', '4:27-4:33', '4:34-4:37', '4:38-4:44', '4:45-4:51', '4:52-4:59', '4:60-4:65', '4:66-4:74', '4:75-4:79', '4:80-4:86', '4:87-4:91', '4:92-4:94', '4:95-4:101', '4:102-4:105', '4:106-4:113', '4:114-4:121', '4:122-4:127', '4:128-4:134', '4:135-4:140', '4:141-4:147', '4:148-4:154', '4:155-4:162', '4:163-4:170', '4:171-4:175', '4:176-5:2', '5:3-5:5', '5:6-5:9', '5:10-5:13', '5:14-5:17', '5:18-5:23', '5:24-5:31', '5:32-5:36', '5:37-5:41', '5:42-5:45', '5:46-5:50', '5:51-5:57', '5:58-5:64', '5:65-5:70', '5:71-5:76', '5:77-5:82', '5:83-5:89', '5:90-5:95', '5:96-5:103', '5:104-5:108', '5:109-5:113', '5:114-5:120', '6:1-6:8', '6:9-6:18', '6:19-6:27', '6:28-6:35', '6:36-6:44', '6:45-6:52', '6:53-6:59', '6:60-6:68', '6:69-6:73', '6:74-6:81', '6:82-6:90', '6:91-6:94', '6:95-6:101', '6:102-6:110', '6:111-6:118', '6:119-6:124', '6:125-6:131', '6:132-6:137', '6:138-6:142', '6:143-6:146', '6:147-6:151', '6:152-6:157', '6:158-6:165', '7:1-7:11', '7:12-7:22', '7:23-7:30', '7:31-7:37', '7:38-7:43', '7:44-7:51', '7:52-7:57', '7:58-7:67', '7:68-7:73', '7:74-7:81', '7:82-7:87', '7:88-7:95', '7:96-7:104', '7:105-7:120', '7:121-7:130', '7:131-7:137', '7:138-7:143', '7:144-7:149', '7:150-7:155', '7:156-7:159', '7:160-7:163', '7:164-7:170', '7:171-7:178', '7:179-7:187', '7:188-7:195', '7:196-7:206', '8:1-8:8', '8:9-8:16', '8:17-8:25', '8:26-8:33', '8:34-8:40', '8:41-8:45', '8:46-8:52', '8:53-8:61', '8:62-8:69', '8:70-8:75', '9:1-9:6', '9:7-9:13', '9:14-9:20', '9:21-9:26', '9:27-9:31', '9:32-9:36', '9:37-9:40', '9:41-9:47', '9:48-9:54', '9:55-9:61', '9:62-9:68', '9:69-9:72', '9:73-9:79', '9:80-9:86', '9:87-9:93', '9:94-9:99', '9:100-9:106', '9:107-9:111', '9:112-9:117', '9:118-9:122', '9:123-9:129', '10:1-10:6', '10:7-10:14', '10:15-10:20', '10:21-10:25', '10:26-10:33', '10:34-10:42', '10:43-10:53', '10:54-10:61', '10:62-10:70', '10:71-10:78', '10:79-10:88', '10:89-10:97', '10:98-10:106', '10:107-11:5', '11:6-11:12', '11:13-11:19', '11:20-11:28', '11:29-11:37', '11:38-11:45', '11:46-11:53', '11:54-11:62', '11:63-11:71', '11:72-11:81', '11:82-11:88', '11:89-11:97', '11:98-11:108', '11:109-11:117', '11:118-12:4', '12:5-12:14', '12:15-12:22', '12:23-12:30', '12:31-12:37', '12:38-12:43', '12:44-12:52', '12:53-12:63', '12:64-12:69', '12:70-12:78', '12:79-12:86', '12:87-12:95', '12:96-12:103', '12:104-12:111', '13:1-13:5', '13:6-13:13', '13:14-13:18', '13:19-13:28', '13:29-13:34', '13:35-13:42', '13:43-14:5', '14:6-14:10', '14:11-14:18', '14:19-14:24', '14:25-14:33', '14:34-14:42', '14:43-14:52', '15:1-15:15', '15:16-15:31', '15:32-15:51', '15:52-15:70', '15:71-15:90', '15:91-16:6', '16:7-16:14', '16:15-16:26', '16:27-16:34', '16:35-16:42', '16:43-16:54', '16:55-16:64', '16:65-16:72', '16:73-16:79', '16:80-16:87', '16:88-16:93', '16:94-16:102', '16:103-16:110', '16:111-16:118', '16:119-16:128', '17:1-17:7', '17:8-17:17', '17:18-17:27', '17:28-17:38', '17:39-17:49', '17:50-17:58', '17:59-17:66', '17:67-17:75', '17:76-17:86', '17:87-17:96', '17:97-17:104', '17:105-18:4', '18:5-18:15', '18:16-18:20', '18:21-18:27', '18:28-18:34', '18:35-18:45', '18:46-18:53', '18:54-18:61', '18:62-18:74', '18:75-18:83', '18:84-18:97', '18:98-18:110', '19:1-19:11', '19:12-19:25', '19:26-19:38', '19:39-19:51', '19:52-19:64', '19:65-19:76', '19:77-19:95', '19:96-20:12', '20:13-20:37', '20:38-20:51', '20:52-20:64', '20:65-20:76', '20:77-20:87', '20:88-20:98', '20:99-20:113', '20:114-20:125', '20:126-20:135', '21:1-21:10', '21:11-21:24', '21:25-21:35', '21:36-21:44', '21:45-21:57', '21:58-21:72', '21:73-21:81', '21:82-21:90', '21:91-21:101', '21:102-21:112', '22:1-22:5', '22:6-22:15', '22:16-22:23', '22:24-22:30', '22:31-22:38', '22:39-22:46', '22:47-22:55', '22:56-22:64', '22:65-22:72', '22:73-22:78', '23:1-23:17', '23:18-23:27', '23:28-23:42', '23:43-23:59', '23:60-23:74', '23:75-23:89', '23:90-23:104', '23:105-23:118', '24:1-24:10', '24:11-24:20', '24:21-24:27', '24:28-24:31', '24:32-24:36', '24:37-24:43', '24:44-24:53', '24:54-24:58', '24:59-24:61', '24:62-25:2', '25:3-25:11', '25:12-25:20', '25:21-25:32', '25:33-25:43', '25:44-25:55', '25:56-25:67', '25:68-25:77', '26:1-26:19', '26:20-26:39', '26:40-26:60', '26:61-26:83', '26:84-26:111', '26:112-26:136', '26:137-26:159', '26:160-26:183', '26:184-26:206', '26:207-26:227', '27:1-27:13', '27:14-27:22', '27:23-27:35', '27:36-27:44', '27:45-27:55', '27:56-27:63', '27:64-27:76', '27:77-27:88', '27:89-28:5', '28:6-28:13', '28:14-28:21', '28:22-28:28', '28:29-28:35', '28:36-28:43', '28:44-28:50', '28:51-28:59', '28:60-28:70', '28:71-28:77', '28:78-28:84', '28:85-29:6', '29:7-29:14', '29:15-29:23', '29:24-29:30', '29:31-29:38', '29:39-29:45', '29:46-29:52', '29:53-29:63', '29:64-30:5', '30:6-30:15', '30:16-30:24', '30:25-30:32', '30:33-30:41', '30:42-30:50', '30:51-30:60', '31:1-31:11', '31:12-31:19', '31:20-31:28', '31:29-31:34', '32:1-32:11', '32:12-32:20', '32:21-32:30', '33:1-33:6', '33:7-33:15', '33:16-33:22', '33:23-33:30', '33:31-33:35', '33:36-33:43', '33:44-33:50', '33:51-33:54', '33:55-33:62', '33:63-33:73', '34:1-34:7', '34:8-34:14', '34:15-34:22', '34:23-34:31', '34:32-34:39', '34:40-34:48', '34:49-35:3', '35:4-35:11', '35:12-35:18', '35:19-35:30', '35:31-35:38', '35:39-35:44', '35:45-36:12', '36:13-36:27', '36:28-36:40', '36:41-36:54', '36:55-36:70', '36:71-36:83', '37:1-37:24', '37:25-37:51', '37:52-37:76', '37:77-37:102', '37:103-37:126', '37:127-37:153', '37:154-37:182', '38:1-38:16', '38:17-38:26', '38:27-38:42', '38:43-38:61', '38:62-38:83', '38:84-39:5', '39:6-39:10', '39:11-39:21', '39:22-39:31', '39:32-39:40', '39:41-39:47', '39:48-39:56', '39:57-39:67', '39:68-39:74', '39:75-40:7', '40:8-40:16', '40:17-40:25', '40:26-40:33', '40:34-40:40', '40:41-40:49', '40:50-40:58', '40:59-40:66', '40:67-40:77', '40:78-40:85', '41:1-41:11', '41:12-41:20', '41:21-41:29', '41:30-41:38', '41:39-41:46', '41:47-41:54', '42:1-42:10', '42:11-42:15', '42:16-42:22', '42:23-42:31', '42:32-42:44', '42:45-42:51', '42:52-43:10', '43:11-43:22', '43:23-43:33', '43:34-43:47', '43:48-43:60', '43:61-43:73', '43:74-43:89', '44:1-44:18', '44:19-44:39', '44:40-44:59', '45:1-45:13', '45:14-45:22', '45:23-45:32', '45:33-46:5', '46:6-46:14', '46:15-46:20', '46:21-46:28', '46:29-46:35', '47:1-47:11', '47:12-47:19', '47:20-47:29', '47:30-47:38', '48:1-48:9', '48:10-48:15', '48:16-48:23', '48:24-48:28', '48:29-49:4', '49:5-49:11', '49:12-49:18', '50:1-50:15', '50:16-50:35', '50:36-51:6', '51:7-51:30', '51:31-51:51', '51:52-52:14', '52:15-52:31', '52:32-52:49', '53:1-53:26', '53:27-53:44', '53:45-54:6', '54:7-54:27', '54:28-54:49', '54:50-55:16', '55:17-55:40', '55:41-55:67', '55:68-56:16', '56:17-56:50', '56:51-56:76', '56:77-57:3', '57:4-57:11', '57:12-57:18', '57:19-57:24', '57:25-57:29', '58:1-58:6', '58:7-58:11', '58:12-58:21', '58:22-59:3', '59:4-59:9', '59:10-59:16', '59:17-59:24', '60:1-60:5', '60:6-60:11', '60:12-61:5', '61:6-61:14', '62:1-62:8', '62:9-63:4', '63:5-63:11', '64:1-64:9', '64:10-64:18', '65:1-65:5', '65:6-65:12', '66:1-66:7', '66:8-66:12', '67:1-67:12', '67:13-67:26', '67:27-68:15', '68:16-68:42', '68:43-69:8', '69:9-69:34', '69:35-70:10', '70:11-70:39', '70:40-71:10', '71:11-71:28', '72:1-72:13', '72:14-72:28', '73:1-73:19', '73:20-74:17', '74:18-74:47', '74:48-75:19', '75:20-76:5', '76:6-76:25', '76:26-77:19', '77:20-77:50', '78:1-78:30', '78:31-79:15', '79:16-79:46', '80:1-80:42', '81:1-81:29', '82:1-83:6', '83:7-83:34', '83:35-84:25', '85:1-85:22', '86:1-87:15', '87:16-88:26', '89:1-89:23', '89:24-90:20', '91:1-92:14', '92:15-94:8', '95:1-96:19', '97:1-98:7', '98:8-100:9', '100:10-102:8', '103:1-105:5', '106:1-108:3', '109:1-111:5', '112:1-114:6']
