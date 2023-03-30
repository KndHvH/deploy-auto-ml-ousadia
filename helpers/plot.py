import matplotlib.pyplot as plt

def create_bar_chart(x, y, title="", x_label="", y_label=""):
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt

def create_line_chart(x, y, title="", x_label="", y_label=""):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt

def create_scatter_chart(x, y, title="", x_label="", y_label=""):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt
