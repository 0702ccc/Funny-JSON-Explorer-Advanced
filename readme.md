# Funny JSON Explorer 设计文档（进阶）    		

​																								——  李俊陶 21307184

### 概述

**Funny JSON Explorer (FJE)** 是一个命令行工具，用于以可视化方式显示 JSON 文件的内容。用户可以选择不同的展示风格（如树形或矩形）和不同的图标族（用于中间节点和叶节点的图标），使用了迭代器以及策略模式进行设计。

### 基本使用方法

```
shell
python jfe.py -f test.json -s tree -i pocker
```

### 示例输入和输出

输入的 JSON 数据：

```json
test.json{
    "oranges": {
        "mandarin": {
            "clementine": null,
            "tangerine": "cheap & juicy!"
        }
    },
    "apples": {
        "gala": null,
        "pink lady": null
    }
}
```

树形展示风格（tree）：

<img src="D:\大学学习资料\大三下\软件工程\design patter\1.png">

<img src="D:\大学学习资料\大三下\软件工程\design patter\3.png">

矩形展示风格（rectangle）：

<img src="D:\大学学习资料\大三下\软件工程\design patter\2.png">

<img src="D:\大学学习资料\大三下\软件工程\design patter\4.png">

### 类图

具体清晰类图见附件中的 `design-uml.png`。



### 类图说明

基于上一个实验进行改进，设置了新的模块：**`Strategy` 和 `Iterator`，对应于策略模式和迭代器模式**（用红色标出）。

- **Strategy（抽象类）**：

  - `execute()`: 抽象方法：运行策略

  - `set_container()`: 抽象方法：设置具体的容器类。
  - `set_leaf()`: 抽象方法：设置具体的叶节点类。

- **Strategy和 RectangleStyleJsonFactory（具体类）**：

  - `execute()`: 具体方法：运行策略

  - `set_container()`: 具体方法：设置具体的容器类。
  - `set_leaf()`: 具体方法：设置具体的叶节点类。

- **Context**

  - `set_strategy()`: 具体方法，设置具体策略。
  - `execute_strategy`：具体方法，运行具体策略。

- **Iterator（抽象类）**：
  - `getNext()`: 抽象方法，获取迭代器下一个目标。
  - `hasMore()`: 抽象方法，是否为最后一个迭代目标。
  
- **Iterator_node**：

  - `getNext()`: 具体实现方法，获取迭代器下一个目标。
  - `hasMore()`: 具体实现方法，是否为最后一个迭代目标。

- **IteratorCollection（抽象类）:**
  - `create_iterator():` 抽象方法，创建迭代器。
  
- **JSONIteratorCollection**

  - `create_iterator():` 具体方法，创建相应迭代器。

其余类复用上一个实验当中实现，因此不再赘述。



### 设计模式说明

#### 一：策略模式（Strategy）

​	策略模式旨在定义一系列算法或行为，将它们各自封装在独立的策略类中，并且使得这些算法或行为可以互相替换，独立于使用它们的客户端代码。通过策略模式，可以在运行时选择不同的算法，从而提高代码的灵活性和可维护性。

​	本次实验中涉及的主要组件：

- **策略接口 (Strategy Interface)**：一个抽象基类，定义了所有策略类必须实现的一系列方法接口。`Strategy` 类定义了 `execute`、`execute_container` 和 `execute_leaf` 三个方法。

- **具体策略类 (Concrete Strategy Classes)**：实现策略接口的具体类，每个类封装了一个特定的算法或行为。有 `Strategy_tree` 和 `Strategy_rectangle` 两个具体策略类，分别实现了树风格和矩形风格的产品构建方法。

- **上下文类 (Context Class)**：持有一个策略对象的引用，通过策略接口与策略对象进行交互。上下文类提供了 `set_strategy` 方法以动态地设置或更换策略，并通过 `execute_strategy` 方法调用策略对象的具体实现。

​	在运行时，根据外部条件（如用户输入）选择合适的策略，通过上下文类的 `set_strategy` 方法设置策略。上下文类的 `execute` 方法负责调用策略对象的相应方法，执行策略定义的算法，并返回结果。

#### 二：迭代器模式（Iterator）

​	迭代器模式旨在提供一种方法，顺序访问一个聚合对象中的各个元素，而又不暴露该对象的内部表示。它将遍历行为从聚合对象中分离出来，使得遍历操作可以独立于聚合对象而变化。

​	本次实验中涉及的主要组件：

- **迭代器接口 (Iterator Interface)**：一个抽象基类，定义了遍历聚合对象所需的基本方法。Iterator` 类定义了 `getNext` 和 `hasMore` 两个方法。

- **具体迭代器类 (Concrete Iterator Class)**：实现迭代器接口的具体类，负责遍历聚合对象中的元素。IteratorNode` 类实现了 `Iterator` 接口，提供了遍历树形节点的具体实现。

- **聚合对象接口 (Aggregate Interface)**：一个抽象基类，定义了创建迭代器的方法。`IteratorCollection` 类定义了 `create_iterator` 方法。
- **具体聚合对象类 (Concrete Aggregate Class)**：实现聚合对象接口的具体类，负责存储和管理元素，并定义创建迭代器的方法JSONIteratorCollection` 类实现了 `IteratorCollection` 接口，提供了创建 JSON 结构的迭代器的方法。

​	通过定义聚合对象类，实现具体迭代器类，并提供创建迭代器实例的方法，客户端可以使用迭代器接口方法（如 `getNext` 和 `hasMore`）遍历集合元素，并无需关注内部实现细节。

#### 三：组合模式（Composite）

​	仍然与上次实验中一致，设置组合模式如下。Composite 模式通过三个关键角色实现：抽象构件（Component）、叶子构件（Leaf）、容器构件（Container）。抽象构件定义了叶子构件和容器构件对象的公共接口，其中包含了所有子类共有的行为。叶子构件表示 JSON 结构中的叶子节点，而容器构件表示 JSON 结构中的容器节点，可以包含多个子节点，这些子节点可以是叶子节点或其他容器节点。

### 添加新的风格

​	通过策略模式实现了展示风格的灵活扩展。这一设计保证了在不改变现有代码的情况下，**只需添加新的策略并相应设置上下文**，就能够轻松地引入新的展示风格。为了实现新的展示风格：需要新增一个具体的产品（product）类，并与相应策略关联在一起。

### 添加新的图标族

只需要在config.json中按照格式加入`icon_container`和`icon_leaf`的图标，并将名字放入主函数中即可：

config.json

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

