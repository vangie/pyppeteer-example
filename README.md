# Pyppeteer 函数计算示例

## 依赖工具

本项目是在 MacOS 下开发的，涉及到的工具是平台无关的，对于 Linux 和 Windows 桌面系统应该也同样适用。在开始本例之前请确保如下工具已经正确的安装，更新到最新版本，并进行正确的配置。

* [Docker](https://www.docker.com/)
* [Fun](https://github.com/aliyun/fun)

Fun 工具依赖于 docker 来模拟本地环境。

对于 MacOS 用户可以使用 [homebrew](https://brew.sh/) 进行安装：

```bash
brew cask install docker
brew tap vangie/formula
brew install fun
```

Windows 和 Linux 用户安装请参考：

1. https://github.com/aliyun/fun/blob/master/docs/usage/installation.md
2. https://github.com/aliyun/fcli/releases

安装好后，记得先执行 `fun config` 初始化一下配置。

**备注**: 本文介绍的技巧需要 Fun 版本大于等于 3.6.8。

## 初始化

```bash
git clone 
```

## 安装依赖

```bash
fun install
```

## 本地运行

```bash
fun install invoke
```

## 部署

```bash
$ fun nas sync
$ fun deploy
```
## 调用

```bash
fun invoke
```