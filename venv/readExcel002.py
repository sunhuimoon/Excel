import openpyxl

if __name__ == '__main__':
    wb = openpyxl.Workbook()
    # 当前打开的sheet页 wb.active
    ws = wb.active

    # 一个文件创建多个表格
    # #更改默认名称Sheet`
    ws.title = "WorkSheetTitle"
    ws.sheet_properties.tabColor = "1072BA"
    # 定义第二个sheet页
    ws2 = wb.create_sheet("NewWorkSheet2")
    ws2.sheet_properties.tabColor = "1072BA"
    # 定义第三个sheet页
    # `0` 的设定 会将该sheet页 置于wb最前面
    ws3 = wb.create_sheet("NewWorkSheet3", 0)

    # 给单元格赋值的方法
    # 方式一：数据可以直接分配到单元格中(可以输入公式)
    ws3['A1'] = 42
    ws["A1"] = "HOGE"
    ws["B1"] = "FUGA"
    # 指定行列给单元格赋值
    ws.cell(row=4, column=2, value=10)
    # 指定行列给单元格赋值
    v = 0
    for i in range(1, 10):
        for n in range(1, 10):
            ws2.cell(row=i, column=n, value=v)
            v += 1

    column_title = ["FirstName", "LastName"]  # 这个可以放在上面
    # column名和値顺序放入单元格中
    rows = [
        column_title,
        ["Tarou", "Tanaka"],
        ["Tarou", "Suzuki"],
        ["Tarou", "Uchiayama"],
        ['nihao', 'buhao']
    ]
    for row in rows:
        ws.append(row)

    # 单元格内换行
    ws['A3'] = "A\nB\nC\nD"
    ws['A3'].alignment = openpyxl.styles.Alignment(wrapText=True)  # 这个必须要

    # 保存
    wb.save('example.xlsx')
