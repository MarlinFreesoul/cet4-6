from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "CET4_两周学习系统.xlsx"

NAVY = "1F4E78"
BLUE = "D9EAF7"
PALE = "EDF4F8"
YELLOW = "FFF2CC"
GREEN = "E2F0D9"
RED = "FCE4D6"
GRAY = "E7E6E6"
WHITE = "FFFFFF"
THIN = Side(style="thin", color="B7B7B7")


def style_header(ws, row=1):
    for cell in ws[row]:
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.font = Font(color=WHITE, bold=True)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
    ws.row_dimensions[row].height = 32


def style_range(ws):
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def widths(ws, mapping):
    for col, width in mapping.items():
        ws.column_dimensions[col].width = width


calendar_rows = [
    (1, "导学1：课程标准与分数", "G01–G03", "读大纲定位、卷面结构、常模分数", "手绘四板块结构与分值", "建立官方要求/系统方法/未验证三栏笔记", "能解释710、无及格线、630+/650+目标"),
    (2, "导学2：听力", "G04、G09", "学官方听力目标、材料类型与一次播放流程", "只分析Directions和选项差异", "听1段时看文字稿，标主旨/细节/转折/态度", "听力证据清单；不记录正确率"),
    (3, "导学3：阅读", "G05、G08", "学三种题型和官方阅读技能", "示范词性槽、锚点、证据句", "拆3个长句并复述逻辑关系", "阅读题型决策树"),
    (4, "导学4：写作", "G06", "学审题四问与30分钟流程", "W01只做审题和三段提纲", "比较两个立场提纲并检查任务维度", "一页写作检查表"),
    (5, "导学5：翻译", "G07", "学意群切分、定主谓、信息核对", "T01只切意群和定主谓", "选3句比较多种自然表达", "一页翻译检查表"),
    (6, "导学6：考场系统", "G10–G12", "学作答顺序、时间边界和错误代码", "模拟填写一次答题记录", "制作个人答题页：时间/信心/证据/错因", "可复用答题记录模板"),
    (7, "导学结业检查", "G01–G12闭卷", "完成12题并立即重答错题", "口述四板块考什么/怎么做/怎么验", "未达10/12回看大纲；达标才进入首刷", "导学≥10/12；首刷准入"),
    (8, "第一次刷题：听力", "无", "2026/06第1套Q1–10一遍作答并记信心", "证据回听与L01–L10订正", "完成Q1–25并逐题写错因", "第一份真实首答数据"),
    (9, "第一次刷题：阅读A/B", "Day8 D+1", "V01–V10首答，先写词性槽", "加M01–M10，先强后弱", "全部订正并建D+1/D+3/D+7队列", "选词/匹配首答正确率与用时"),
    (10, "第一次刷题：仔细阅读", "Day8 D+1", "R01–R05首答并写定位句", "加R06–R10", "逐项解释错误选项为什么错", "仔细阅读正确率、证据定位率"),
    (11, "第一次输出：写作", "Day8 D+3；Day9 D+1", "W01限时30分钟首稿", "用8分量表自评并修订", "写W02提纲并提取重复错误", "原稿、量表、修订稿"),
    (12, "第一次输出：翻译", "Day9 D+3；Day10 D+1", "T01限时30分钟", "检查信息块并修订", "用T02做3句迁移", "原稿、漏译率、修订稿"),
    (13, "首轮复盘", "到期D+1/D+3", "重做到期项并更新错因", "汇总四板块Top 3瓶颈", "最低项做一组换材料迁移", "首答与复测对照、瓶颈清单"),
    (14, "第一次整卷", "导学与流程回忆", "30分钟流程回忆；无连续时段则改复测日", "不把60分钟分段题称为完整模拟", "连续约150分钟：2025/12第1套125分钟+复盘25", "首次完整基线；分段须标非模拟"),
]


guide = [
    ("G01", "CET4报道总分满分是多少？", "710", "官方报道分上限，不是简单卷面百分数。", "官方分数解释"),
    ("G02", "CET4是否设官方及格线？", "不设", "采用常模参照报道分；其他机构要求不等于官方及格线。", "官方分数解释"),
    ("G03", "听力、阅读、写译的占比和满分？", "听力35%/249；阅读35%/249；写译30%/212", "四个单项相加为710；写作与翻译合并报道。", "官方分数解释"),
    ("G04", "官方听力能力除听见单词外还考什么？", "主旨、细节、隐含意义、交际功能、观点态度、语音与句间关系", "复盘必须写证据类型。", "官方考试大纲"),
    ("G05", "官方阅读能力包含哪些核心动作？", "主旨、细节、观点态度、推断、猜词、句间关系、篇章衔接", "三种阅读题型都回到这些动作。", "官方考试大纲"),
    ("G06", "四级写作最低官方产出要求？", "30分钟，不少于120词；中心明确、结构完整、通顺连贯", "当次题面若给上限，以当次Directions为准。", "官方考试大纲"),
    ("G07", "四级翻译官方要求？", "30分钟，140–160汉字熟悉题材汉译英，基本准确通顺", "检查信息完整和英语自然，不逐字替换。", "官方考试大纲"),
    ("G08", "仔细阅读与快速阅读目标速度？", "约70词/分钟；100词/分钟", "速度必须和理解同时测。", "官方考试大纲"),
    ("G09", "四级听力材料官方语速？", "约120–140词/分钟", "辅助材料可参考该区间，真题仍优先。", "官方考试大纲"),
    ("G10", "高考135/150能否直接换成CET639/710？", "不能；639只是90%的算术类比", "CET为常模参照；630约第98百分位，650约第99。", "官方分数解释"),
    ("G11", "什么算完整四级模拟？", "连续按正式流程完成125分钟；听力一次播放", "分段训练必须标非完整模拟。", "官方卷面结构+系统规则"),
    ("G12", "本系统真题客观答案是什么身份？", "第三方参考答案", "不是官方标准答案；冲突时标争议。", "资料库来源边界"),
]


listening = [
    ("L01", 1, "C", "儿子从多家餐馆下单导致账单；主语和行为完整对应。", "19"),
    ("L02", 2, "B", "结尾明确说父亲打算更改密码。", "20"),
    ("L03", 3, "A", "研究考察游客如何影响动物行为。", "21"),
    ("L04", 4, "D", "正确项保留动物在动物园出生并长大的限定。", "22"),
    ("L05", 5, "B", "项目状态是暂停，而非调整、重评或扩张。", "24"),
    ("L06", 6, "D", "合资格者可获得1,200美元；数字和条件都要保留。", "24"),
    ("L07", 7, "C", "后续动作是恢复电动自行车激励项目。", "25"),
    ("L08", 8, "A", "对话指向coin collection。", "27"),
    ("L09", 9, "A", "街道狭窄但漂亮，对应charming。", "28"),
    ("L10", 10, "B", "该地点被描述为著名且漂亮。", "29"),
]

vocab = [
    ("V01", 26, "N squeezed", "过去式谓语；squeeze ... from ...搭配与负面语境共同锁定。", "62"),
    ("V02", 27, "A available", "with复合结构；available to为固定搭配。", "63"),
    ("V03", 28, "I increased", "主语后缺谓语，语境说明生活水平提高。", "63"),
    ("V04", 29, "K occurred", "improvement后需不及物谓语。", "64"),
    ("V05", 30, "F exactly", "副词修饰define，表示准确界定。", "64"),
    ("V06", 31, "O typically", "副词修饰use，表示通常使用。", "65"),
    ("V07", 32, "C earned", "过去分词后置修饰money。", "65"),
    ("V08", 33, "G exhausting", "形容词修饰debate，表示耗费精力。", "66"),
    ("V09", 34, "J interpret", "decided to后接原形，语义为解释影响。", "67"),
    ("V10", 35, "D effect", "positive后需名词；positive effect搭配成立。", "67"),
]

matching_answers = ["C", "I", "E", "L", "A", "F", "J", "B", "D", "G"]
matching = []
for idx, answer in enumerate(matching_answers, start=36):
    strength = "弱锚点；最后做，靠整句语义确认。" if idx == 44 else "强锚点；先定位独特词，再核对整句同义改写。"
    page = "81" if idx >= 44 else str(77 + (idx - 36) // 2)
    matching.append((f"M{idx-35:02d}", idx, f"{answer}段", strength, page))

reading_explanations = [
    (46, "D", "两难两侧都要保留：最好食物+预算有限。", "93"),
    (47, "A", "won't give a clear-cut answer同义为仍不确定。", "94"),
    (48, "D", "食品安全角度没有实质差别；有机种植也用农药。", "95"),
    (49, "C", "smaller environmental footprint对应环境影响更小。", "96"),
    (50, "B", "更多研究和资金是条件，产量效率提高是结果。", "97"),
    (51, "A", "自私在短期可能有利；short-lived限定时间。", "104"),
    (52, "B", "双胞胎研究提供行为受基因影响的强证据，但非完全决定。", "105"),
    (53, "C", "识别出与利他行为相关的特定基因。", "106"),
    (54, "A", "evolved first among relatives对应起源于血亲个体。", "107"),
    (55, "D", "文化、教育和养育影响合作，因此可后天培养。", "108-109"),
]
reading = [(f"R{q-45:02d}", q, ans, exp, pg) for q, ans, exp, pg in reading_explanations]

production = [
    ("W01", "写作", "2026/06 第1套", "PDF第1页", "限时回应：大学生是否应至少参加一个研究项目；同时讨论必要性和可行性。", "任务覆盖必要性+可行性；中心明确；120–180词；限时30分钟。", "中心句可同时给立场与可行条件；只写重要性属于任务遗漏。"),
    ("W02", "写作", "2026/06 第2套", "PDF第1页", "限时写校园机器人未来应用投稿。", "具体应用+学生收益+风险边界；120–180词；30分钟。", "用assist rather than replace human judgment限制过度主张。"),
    ("W03", "写作", "2025/12 第1套", "PDF第1页", "给学生会提出丰富校园生活的建议。", "建议必须指向学生会且可执行；120–180词；30分钟。", "机制、行动、反馈比泛泛口号更完整。"),
    ("T01", "翻译", "2026/06 第1套", "PDF第10–11页", "限时翻译尊师传统段落。", "覆盖俗语、教师角色、古代仪式、1985教师节、当代传承。", "先切意群；俗语可意译并说明；日期与因果不得漏。"),
    ("T02", "翻译", "2026/06 第2套", "PDF第10–11页", "限时翻译餐桌礼仪段落。", "覆盖文化地位、备菜、座次、席间招待、延续与人际功能。", "按客人口味、座次方位和作用分别成句，避免逐字硬译。"),
    ("T03", "翻译", "2025/12 第2套", "PDF末页", "限时翻译城市漫步段落。", "覆盖新趋势、与传统旅游对比、活动与文化理解。", "Unlike引对比；活动列表保持平行结构。"),
]


def build():
    wb = Workbook()
    ws = wb.active
    ws.title = "设置与状态"
    ws.append(["字段", "填写值", "状态/说明"])
    settings = [
        ("计划开始日", date(2026, 9, 23), "可修改；14天日历日期会随之更新"),
        ("每日计划保底分钟", 30, "用户指定：0.5小时"),
        ("每日弹性容量分钟", 120, "用户确认：至少2小时以上；120为保守记录"),
        ("计划考试日", date(2026, 12, 12), "用户提供；最终以官方公告/准考证为准"),
        ("目标", "主目标630+；冲刺650+", "满分710；630约第98百分位，650约第99"),
        ("理论满分", 710, "官方报道总分满分；采用常模参照，不设及格线"),
        ("当前阶段", "导学准备，尚未首刷", "Day1–7导学；达10/12后进入首刷"),
        ("听力基线", "待Day8首刷", "不以跟做示范作为基线"),
        ("阅读基线", "待Day9–10首刷", "分别记录三种题型"),
        ("写作基线", "待Day11首稿", "用本系统8分训练量表"),
        ("翻译基线", "待Day12首稿", "用本系统8分训练量表"),
        ("课程标准", "全国大学英语四、六级考试大纲", "用户确认：同时作为考试标准与命题标准"),
        ("课堂讲义", "无", "用户确认"),
        ("指定阅读", "无", "用户确认"),
        ("额外课程题集", "无", "使用当前真题资料库"),
        ("历次小测", "无", "用户确认；尚未首刷"),
        ("建议执行档", '=IF(B3<=30,"30分钟保底；按120+分钟容量自愿扩展","自定义保底")', "保底不是上限；完整模拟需连续约150分钟"),
    ]
    for row in settings:
        ws.append(row)
    style_header(ws)
    style_range(ws)
    for row in range(2, len(settings) + 2):
        ws.cell(row=row, column=2).fill = PatternFill("solid", fgColor=YELLOW)
    ws["B2"].number_format = "yyyy-mm-dd"
    ws["B5"].number_format = "yyyy-mm-dd"
    ws.freeze_panes = "A2"
    widths(ws, {"A": 22, "B": 22, "C": 58})

    cal = wb.create_sheet("14天日历")
    cal.append(["Day", "日期", "阶段", "导学题/到期复习", "30分钟保底", "扩展到60分钟", "使用120+分钟容量", "可验证产出", "完成状态", "实际分钟", "正确率/得分", "错误代码/备注", "下次复习日"])
    for i, item in enumerate(calendar_rows, start=0):
        day_no, new_task, due, core, standard, full, artifact = item
        row = cal.max_row + 1
        cal.append([
            day_no,
            f"='设置与状态'!$B$2+{i}",
            new_task,
            due,
            core,
            standard,
            full,
            artifact,
            "未开始",
            "",
            "",
            "",
            "",
        ])
        cal.cell(row=row, column=2).number_format = "yyyy-mm-dd ddd"
    style_header(cal)
    style_range(cal)
    cal.freeze_panes = "A2"
    cal.auto_filter.ref = f"A1:M{cal.max_row}"
    status_dv = DataValidation(type="list", formula1='"未开始,进行中,已完成,跳过"', allow_blank=False)
    cal.add_data_validation(status_dv)
    status_dv.add(f"I2:I{cal.max_row}")
    cal.conditional_formatting.add(f"I2:I{cal.max_row}", CellIsRule(operator="equal", formula=['"已完成"'], fill=PatternFill("solid", fgColor=GREEN)))
    cal.conditional_formatting.add(f"I2:I{cal.max_row}", CellIsRule(operator="equal", formula=['"跳过"'], fill=PatternFill("solid", fgColor=RED)))
    widths(cal, {"A": 7, "B": 15, "C": 29, "D": 21, "E": 34, "F": 31, "G": 32, "H": 30, "I": 11, "J": 11, "K": 14, "L": 26, "M": 15})

    bank = wb.create_sheet("题库")
    bank.append(["ID", "板块", "来源", "题位", "任务", "计划日", "首次答案", "首次对错", "信心1-4", "错误代码", "证据/理由", "D+1", "D+3", "D+7", "状态"])
    q_rows = []
    guide_days = {"G01": 1, "G02": 1, "G03": 1, "G04": 2, "G09": 2, "G05": 3, "G08": 3, "G06": 4, "G07": 5, "G10": 6, "G11": 6, "G12": 6}
    for item_id, question, _answer, _exp, source in guide:
        q_rows.append((item_id, "大纲导学", source, "导学题", question, guide_days[item_id]))
    for item_id, q, _ans, _exp, _pg in listening:
        q_rows.append((item_id, "听力", "2026/06 第1套", f"真题PDF第{1 if q <= 4 else 2 if q <= 11 else 3}页 / 题{q}", f"播放本地MP3，一遍作答第{q}题，并记录证据词。", 8))
    for item_id, q, _ans, _exp, _pg in vocab:
        q_rows.append((item_id, "选词填空", "2026/06 第1套", f"真题PDF第5–6页 / 题{q}", f"完成第{q}题；先写词性槽，再选词。", 9))
    for item_id, q, _ans, _exp, _pg in matching:
        q_rows.append((item_id, "长篇匹配", "2026/06 第1套", f"真题PDF第7页 / 题{q}", f"完成第{q}题；圈强锚点并写同义替换。", 9))
    for item_id, q, _ans, _exp, _pg in reading:
        q_rows.append((item_id, "仔细阅读", "2026/06 第1套", f"真题PDF第{8 if q <= 47 else 9 if q <= 50 else 10}页 / 题{q}", f"完成第{q}题；写题型和定位句。", 10))
    for item_id, section, src, loc, task, _answer, _exp in production:
        planned = {"W01": 11, "W02": 11, "W03": 11, "T01": 12, "T02": 12, "T03": 12}[item_id]
        q_rows.append((item_id, section, src, loc, task, planned))
    for item_id, section, src, loc, task, planned in q_rows:
        bank.append([item_id, section, src, loc, task, planned, "", "", "", "", "", "", "", "", "未开始"])
    style_header(bank)
    style_range(bank)
    bank.freeze_panes = "A2"
    bank.auto_filter.ref = f"A1:O{bank.max_row}"
    yn_dv = DataValidation(type="list", formula1='"正确,错误,猜对,未答"')
    state_dv = DataValidation(type="list", formula1='"未开始,已首答,复习中,暂时掌握,争议"')
    confidence_dv = DataValidation(type="whole", operator="between", formula1="1", formula2="4")
    for dv in (yn_dv, state_dv, confidence_dv):
        bank.add_data_validation(dv)
    yn_dv.add(f"H2:H{bank.max_row}")
    state_dv.add(f"O2:O{bank.max_row}")
    confidence_dv.add(f"I2:I{bank.max_row}")
    bank.conditional_formatting.add(f"H2:H{bank.max_row}", CellIsRule(operator="equal", formula=['"正确"'], fill=PatternFill("solid", fgColor=GREEN)))
    bank.conditional_formatting.add(f"H2:H{bank.max_row}", CellIsRule(operator="equal", formula=['"错误"'], fill=PatternFill("solid", fgColor=RED)))
    widths(bank, {"A": 9, "B": 13, "C": 18, "D": 24, "E": 44, "F": 9, "G": 14, "H": 11, "I": 10, "J": 14, "K": 35, "L": 12, "M": 12, "N": 12, "O": 13})

    ans = wb.create_sheet("答案解析")
    ans.append(["ID", "答案/达标条件", "简析", "来源位置", "证据等级"])
    for item_id, question, answer, exp, source in guide:
        ans.append([item_id, answer, exp, source, "官方大纲/官方分数解释；G12为资料边界"])
    for item_id, q, answer, exp, pg in listening:
        ans.append([item_id, answer, exp, f"2026/06第1套第三方解析 PDF第{pg}页", "第三方参考；题面已视觉抽查"])
    for item_id, q, answer, exp, pg in vocab:
        ans.append([item_id, answer, exp, f"2026/06第1套第三方解析 PDF第{pg}页", "第三方参考；第26题已视觉核验"])
    for item_id, q, answer, exp, pg in matching:
        ans.append([item_id, answer, exp, f"2026/06第1套第三方解析 PDF第{pg}页", "第三方参考"])
    for item_id, q, answer, exp, pg in reading:
        ans.append([item_id, answer, exp, f"2026/06第1套第三方解析 PDF第{pg}页", "第三方参考；第46/51题已视觉核验"])
    for item_id, section, src, loc, task, answer, exp in production:
        ans.append([item_id, answer, exp, f"{src} {loc}", "题干来自本地卷；评价条件为训练量表"])
    style_header(ans)
    style_range(ans)
    ans.freeze_panes = "A2"
    ans.auto_filter.ref = f"A1:E{ans.max_row}"
    widths(ans, {"A": 9, "B": 48, "C": 68, "D": 38, "E": 35})

    prog = wb.create_sheet("进度")
    prog.append(["板块", "题库数", "已首答", "首次正确", "首次正确率", "D+7已测", "D+7正确", "D+7正确率", "平均信心", "主要错误", "下一步"])
    sections = ["大纲导学", "听力", "选词填空", "长篇匹配", "仔细阅读", "写作", "翻译"]
    for idx, section in enumerate(sections, start=2):
        prog.cell(idx, 1, section)
        prog.cell(idx, 2, f'=COUNTIF(题库!$B:$B,A{idx})')
        prog.cell(idx, 3, f'=COUNTIFS(题库!$B:$B,A{idx},题库!$H:$H,"<>" )')
        prog.cell(idx, 4, f'=COUNTIFS(题库!$B:$B,A{idx},题库!$H:$H,"正确")')
        prog.cell(idx, 5, f'=IFERROR(D{idx}/C{idx},"")')
        prog.cell(idx, 6, f'=COUNTIFS(题库!$B:$B,A{idx},题库!$N:$N,"<>" )')
        prog.cell(idx, 7, f'=COUNTIFS(题库!$B:$B,A{idx},题库!$N:$N,"正确")')
        prog.cell(idx, 8, f'=IFERROR(G{idx}/F{idx},"")')
        prog.cell(idx, 9, f'=IFERROR(AVERAGEIF(题库!$B:$B,A{idx},题库!$I:$I),"")')
    for row in range(2, 9):
        prog.cell(row, 5).number_format = "0%"
        prog.cell(row, 8).number_format = "0%"
        prog.cell(row, 9).number_format = "0.0"
    prog.append([])
    prog.append(["结项指标", "导学后首刷基线", "Day13/14结果", "变化", "口径/证据"])
    metric_row = prog.max_row
    metrics = [
        "听力正确率", "阅读正确率", "写作训练量表/8", "翻译训练量表/8", "未完成题数", "重复错误数", "翻译信息遗漏率", "总实际分钟"
    ]
    for metric in metrics:
        prog.append([metric, "", "", f'=IF(OR(B{prog.max_row+1}="",C{prog.max_row+1}=""),"",C{prog.max_row+1}-B{prog.max_row+1})', "请写明题量或评分口径"])
    style_header(prog)
    for c in prog[metric_row]:
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.font = Font(color=WHITE, bold=True)
    style_range(prog)
    prog.freeze_panes = "A2"
    widths(prog, {"A": 22, "B": 12, "C": 12, "D": 12, "E": 14, "F": 12, "G": 12, "H": 14, "I": 12, "J": 25, "K": 28})

    src = wb.create_sheet("来源")
    src.append(["来源ID", "来源", "身份", "用途", "读取状态", "可靠性/限制"])
    source_rows = [
        ("O1", "教育部教育考试院 CET4笔试页面", "官方", "题型、题数、比例、时长", "deep-read", "当前官网公开结构"),
        ("O2", "全国大学英语四六级考试大纲（2016修订版）", "官方/课程标准", "听读写译能力目标与导学", "targeted", "PDF有复制限制；未绕过，本次依赖官方索引文本"),
        ("O3", "教育部教育考试院 分数解释", "官方", "满分、分项、常模百分位、目标设定", "deep-read", "满分710；常模参照；不设及格线"),
        ("P2512", "materials/CET4/2025/12 三套真题", "来源页标注真题", "诊断、迁移、写作翻译", "提示deep-read；其余mapped/sampled", "来源非考试委员会直接分发"),
        ("A2512", "materials/CET4/2025/12 三套答案解析", "第三方", "复盘", "sampled", "非官方标准答案"),
        ("P2606", "materials/CET4/2026/06 三套真题", "来源页标注真题", "主训练题库", "第1套重点deep-read", "来源非考试委员会直接分发"),
        ("A2606", "materials/CET4/2026/06 三套答案解析", "第三方", "答案与解释", "第1套相关题deep-read", "非官方标准答案；未全卷逐页视觉核验"),
        ("SCOPE", "课堂讲义/指定阅读/课程题集/历次小测", "用户确认无", "范围边界", "not-applicable", "大纲作为课程标准；当前真题库作为训练材料"),
        ("TIME", "个人可用学习时间", "用户确认", "日历容量", "confirmed", "计划保底30分钟；实际弹性容量至少120分钟"),
        ("DATE", "2026-12-12考试日", "用户提供", "阶段路线", "官方当次公告未检索到", "最终以官方公告和准考证为准"),
    ]
    for row in source_rows:
        src.append(row)
    style_header(src)
    style_range(src)
    src.freeze_panes = "A2"
    widths(src, {"A": 13, "B": 42, "C": 19, "D": 28, "E": 27, "F": 56})

    for sheet in wb.worksheets:
        sheet.sheet_view.showGridLines = False
        sheet.sheet_properties.pageSetUpPr.fitToPage = True
        sheet.page_setup.fitToWidth = 1
        sheet.page_setup.fitToHeight = 0
        sheet.page_setup.orientation = "portrait" if sheet.title == "设置与状态" else "landscape"
        sheet.page_margins.left = 0.25
        sheet.page_margins.right = 0.25
        sheet.page_margins.top = 0.4
        sheet.page_margins.bottom = 0.4
        sheet.print_title_rows = "1:1"
        sheet.print_area = f"A1:{get_column_letter(sheet.max_column)}{sheet.max_row}"
        for row in range(2, sheet.max_row + 1):
            if row % 2 == 0:
                for cell in sheet[row]:
                    if cell.fill.fill_type is None:
                        cell.fill = PatternFill("solid", fgColor=PALE)
        sheet.auto_filter.ref = sheet.auto_filter.ref or f"A1:{get_column_letter(sheet.max_column)}{sheet.max_row}"

    wb.save(OUTPUT)

    check = load_workbook(OUTPUT, data_only=False)
    expected = {"设置与状态", "14天日历", "题库", "答案解析", "进度", "来源"}
    assert set(check.sheetnames) == expected, check.sheetnames
    assert check["题库"].max_row == 59
    assert check["答案解析"].max_row == 59
    assert check["14天日历"].max_row == 15
    check.close()


if __name__ == "__main__":
    build()
