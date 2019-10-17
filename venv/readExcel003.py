import openpyxl
from openpyxl.styles import Border, Side
from openpyxl.styles import PatternFill
from openpyxl import Workbook, load_workbook

if __name__ == '__main__':
    """
    设置字体font
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    # 更改默认名称Sheet`
    ws.title = "worksheettitle"

    # 设置font
    font = openpyxl.styles.Font(
        name="宋体",
        size=15,
    )
    a1 = ws["A1"]
    a1.font = font
    a1.value = "TEST"

    # 上面要添加from openpyxl.styles import Border, Side
    # 设置单元格border的style
    border = Border(
        left=Side(
            border_style="thin",
            color="FF0000"
        ),
        right=Side(
            border_style="thin",
            color="FF0000"
        ),
        top=Side(
            border_style="thin",
            color="FF0000"
        ),
        bottom=Side(
            border_style="thin",
            color="FF0000"

        )
    )
    b2 = ws["B2"]
    b2.border = border
    b2.value = "TEST"

    # 合并单元格
    ws.merge_cells("C1:E1")
    ws["c1"] = "HOGE"

    # 单元格填充颜色
    # from openpyxl.styles import PatternFill 需要用到这个啦
    fill = PatternFill(fill_type='solid', fgColor='FFFF0000')
    b3 = ws["B3"]
    b3.fill = fill
    b3.value = "TEST"

    # 作成第二个sheet页 名称胃example
    ws2 = wb.create_sheet("example")
    # 设置超链接 到“example”sheet页 鼠标定格在A5单元格
    ws["A4"] = "Link"
    ws["A4"].hyperlink = "example003.xlsx#example!A5"


#from openpyxl import Workbook, load_workbook  加这个
    # 读Excel文档
    wb = load_workbook('./example003.xlsx')
    ws = wb.active
    for row in ws:
        for cell in row:
            print(cell)
    # 保存
    wb.save('example003.xlsx')
