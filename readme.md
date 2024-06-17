# Funny JSON Explorer

Funny JSON Explorer (FJE)，是一个JSON文件可视化的命令行界面小工具（**更新设计模式为：迭代器+策略模式**）

## 安装

基于 `python` 编写，要求用户有能够运行 `python`代码的环境，在根目录下启动终端，运行如下命令即可：

```
python jfe.py -f <json_file_path> -s <style> -i <icon_famlily>
```

完整的命令说明如下：

```
usage: fje [-h] -f FILE [-s STYLE] [-i ICON_FAMILY] [-c CONFIG] [-v]

Funny JSON Explorer

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  JSON file path
  -s STYLE, --style STYLE
                        style
  -i ICON_FAMILY, --icon-family ICON_FAMILY
                        icon family
  -c CONFIG, --config CONFIG
                        icon family file
  -v, --verbose         print availavle icon families and styles
```

配置根目录下的`config.json`文件，即可修改图形族，目前已有图形族如下；

```json
{
  "icon_families": {
    "pocker": {
      "icon_container": "♥",
      "icon_leaf": "♠"
    },
    "star": {
      "icon_container": "★",
      "icon_leaf": "✿"
    },
    "box": {
      "icon_container": "📦",
      "icon_leaf": "🍃"
    }
  }
}
```

## 测试

根目录下提供实验文档中的测试用例（test.json）,可以用示例命令查看运行效果：

```
python jfe.py -f test.json -s tree -i pocker
```
