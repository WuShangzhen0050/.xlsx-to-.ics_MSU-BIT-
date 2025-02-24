# .xlsx-to-.ics_MSU-BIT-2025

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/WuShangzhen0050/.xlsx-to-.ics_MSU-BIT-/blob/main/README.en.md)
[![zh-cn](https://img.shields.io/badge/lang-zh--cn-red.svg)](https://github.com/WuShangzhen0050/.xlsx-to-.ics_MSU-BIT-/blob/main/README.md)



## 项目简介
我们smbu官网（ https://ehall.smbu.edu.cn 还有其中的新版教务系统 ）里面提供的课表只能以.xlsx(Excel)格式导出，我们要把课表导入日历软件的话就很麻烦了。现今我用Python创建一个项目，缓解这个问题。

- **自动化转换**： 该项目允许您将 Excel 课程表转换为 iCalendar (.ics) 文件，
- **兼容性强**： 该文件可以导入 Outlook、Google 日历或其他日历应用。
- **支持自定义**： 用户可修改 `conf_classTime.json` 来调整时间段。

但作者仅在 Outlook 中对其进行了测试。作者是本科数学与应用数学专业的中国学生（编辑时间为2025年02月），非本科、其他专业的课程表可能会有不同之处，相关人员视具体情况自行操作或参考。

作者在编辑时间已经检查过在学校官网把语言调整成Русский язык和English然后下载Excel课程表的情况，结果下载得到的是中文的课程表，所以这里没有这两种语言的方案。

作者对生成的 iCalendar 文件中的任何错误概不负责。

作者在此抛砖引玉，欢迎提出问题或建议，欢迎升级本项目。下面的2个参考项目中有的功能是作者还没有实现的，有兴趣的师生可以前去访问。

本项目参考了以下 GitHub 开源项目：
- [wenchenwan/ClasstableToIcalforNUAA](https://github.com/wenchenwan/ClasstableToIcalforNUAA)
- [miaotony/NUAA_ClassSchedule](https://github.com/miaotony/NUAA_ClassSchedule)

对上述项目的贡献者表示感谢！

---

## 使用方法
开始操作前，请通读一遍README（本文）！本项目是否要专门部署在某容器等问题请自行考量，上面的参考项目也提出了一些方案，但是本项目不必部署在vercel、 虚拟机等复杂容器。

1. **设置**：确保已安装 Python 3。
2. **安装依赖项**：使用以下命令安装所需的软件包：
    ```
    pip install pandas icalendar
    ```
   （conda用户也可以使用conda安装）
3. **准备 Excel 课程表**
   请确保你的 Excel 表格的列中存在：
   - `课程名称`
   - `上课周次`
   - `上课时间`
   - `教室`
   - `主讲教师`
   - `选课人数`

   旧版的课程表（2024年）是如项目中”我的课表.xlsx"那样的，这个项目的旧版本也只能以这种表格文件为输入，旧版的课程表是可以不用调整或几乎不用调整的；但是新版的课程表（2025年）是符合常见的课程表格式的，反而会有调整起来挺麻烦的问题，这个只能由我（但是我即将毕业）或其他用户在issue中或得到我的许可push调校完成的xlsx文件了。

   本次更新就是专门为了课程表改版的问题而做的。

   示例文件请参考 adjusted202502.xlsx。
4. **立即查看课程表的官方规则**:\
   新闻: https://ehall--ps-smbu-edu-cn-s.webvpn.smbu.edu.cn:8118/psfw/sys/tzggapp/*default/index.do?ggdm=d12ecd3a-8096-4dde-926a-ab579a6ad44f#/ggll
   **注意**: What date is the first day of the semester?
5. **查看详情（旧版步骤）**: 查看课程表的详细信息：
    - `课程号`
    - `课程名`
    - `课序号`
    - `开课单位`
    - `学分`
    - `...`
   
   (如有，以上很多信息在新的课程表中检查不到了，但是无妨，我的脚本只涉及最有用的几列信息，“选课人数”之类的信息都没管，如果诸位不满意可以自己调整代码)
6. **反复检查信息**:
    - `上课周次`
    - `开始节次`
    - `结束节次`
    - `...`
7. **运行脚本**:
    ```
    python main.py 你的课表.xlsx --config_file conf_classTime.json --output_file 你的课表.ics --semester_start_date YYYY-MM-DD

    ```
   (这只是一个模板，注意参数要根据你的实际情况变更)
8. **导出文件**: 生成的“***.ics”（文件名是你在第7项步骤自定义的）文件将位于项目目录中。

## 配置

修改`conf_classTime.json`来自定义时间段。

