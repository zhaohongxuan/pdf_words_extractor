# PDF难词单词提取器

这个简单的小程序作用是从PDF中提取难词，并且匹配相应的等级（目前词汇等级有 `雅思IELTS`，`托福TOEFL`,`GRE`）并且输出到Excel文件。功能非常简单，主要是为了方便自己快速的掌握一个文档中的生难词。

## Usage

1. 克隆项目: `https://github.com/zhaohongxuan/pdf_words_extractor.git`
2. 安装依赖:`pip install -r requirements.txt` 或者`pip3 install -r requirements.txt`
3. 更改`extract_pdf.py`中`pdf_file`文件路径为你想要的提取的pdf路径。
4. 在result文件夹找到对应名称的excel文件。

## TODO

- [ ] 支持命令行转换
- [ ] 增加单词在文章中出现的频率
- [ ] 增加单词在COCA中出现的频率
- [ ] 按照分组导入欧陆词典
