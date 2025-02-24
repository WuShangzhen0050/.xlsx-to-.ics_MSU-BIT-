# .xlsx-to-.ics_MSU-BIT-2025

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/WuShangzhen0050/.xlsx-to-.ics_MSU-BIT-/blob/main/README.en.md)
[![zh-cn](https://img.shields.io/badge/lang-zh--cn-red.svg)](https://github.com/WuShangzhen0050/.xlsx-to-.ics_MSU-BIT-/blob/main/README.md)



## 项目简介
我们smbu官网（ https://ehall.smbu.edu.cn ）里面提供的课表只能以.xlsx(Excel)格式导出，我们要把课表导入日历软件的话就很麻烦了。现今我用Python创建一个项目，缓解这个问题。

- **自动化转换**： 该项目允许您将 Excel 课程表转换为 iCalendar (.ics) 文件，
- **兼容性强**： 该文件可以导入 Outlook、Google 日历或其他日历应用。
- **支持自定义**： 用户可修改 `conf_classTime.json` 来调整时间段。
但作者仅在 Outlook 中对其进行了测试。
作者对生成的 iCalendar 文件中的任何错误概不负责。

本项目参考了以下 GitHub 开源项目：
- [wenchenwan/ClasstableToIcalforNUAA](https://github.com/wenchenwan/ClasstableToIcalforNUAA)
- [miaotony/NUAA_ClassSchedule](https://github.com/miaotony/NUAA_ClassSchedule)

对上述项目的贡献者表示感谢！

---

## 使用方法
1. **设置**：确保已安装 Python 3。
2. **安装依赖项**：使用以下命令安装所需的软件包：
    ```
    pip install pandas icalendar
    ```
3. **准备 Excel 课程表**
   请确保你的 Excel 文件符合以下格式：
   课程名称
   上课周次
   上课时间
   教室
   主讲教师
   选课人数

   示例文件请参考 classInfo.xlsx。
4. **立即查看课程表的官方规则**:\
   新闻: https://ehall--ps-smbu-edu-cn-s.webvpn.smbu.edu.cn:8118/psfw/sys/tzggapp/*default/index.do?ggdm=d12ecd3a-8096-4dde-926a-ab579a6ad44f#/ggll
   **注意**: What date is the first day of the semester?
5. **查看详情**: 查看课程表的详细信息：
    - `Course Code`/`课程号`
    - `Course Name`/`课程名`
    - `Section`/`课序号`
    - `开课单位`
    - `学分`
    - `...`
   (如有)
6. **再次检查时间段**: 检查时间段：
    - `上课周次`
    - `开始节次`
    - `结束节次`
    - `...`
7. **运行脚本**:
    ```
    python main.py 你的课表.xlsx --config_file conf_classTime.json --output_file 你的课表.ics --semester_start_date YYYY-MM-DD

    ```
   (这只是一个模板，注意参数要根据你的实际情况变更)
8. **导出文件**: 生成的“class_schedule.ics”文件将位于项目目录中。

## 配置

修改`conf_classTime.json`来自定义时间段。

