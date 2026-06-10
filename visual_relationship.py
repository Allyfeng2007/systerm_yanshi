from pyecharts import options as opts
from pyecharts.charts import Graph
from streamlit_echarts import st_pyecharts


class Relation:
    def draw_realtion(self):
        with open('sucai/红楼梦.txt', encoding='utf-8') as f:
            text = f.read()
        # 红楼梦主要人物别称映射字典
        name_map = {
            '林黛玉': ['黛玉', '林妹妹', '颦儿'],
            '贾宝玉': ['宝玉', '宝兄弟', '宝二爷', '玉兄弟'],
            '薛宝钗': ['宝钗', '宝姐姐'],
            '王熙凤': ['凤姐', '凤姐儿', '熙凤'],
            '贾母': ['老太太'],
            '贾探春': ['探春'],
            '贾迎春': ['迎春'],
            '贾惜春': ['惜春'],
            '秦可卿': ['可卿'],
        }

        # 生成“别名”到“标准名”的反向映射表
        dic = {}
        for k, v in name_map.items():
            for i in v:
                dic[i] =k

        for k, v in dic.items():
            text = text.replace(k, v)

        # 得到人物关系
        Names = ['宝玉','王熙凤','贾母','黛玉','王夫人','袭人','贾琏','平儿','宝钗','薛姨妈','探春','鸳鸯','贾政','晴雯','湘云','刘姥姥','邢夫人','贾珍','紫鹃','香菱','尤氏','薛蟠','贾赦']
        relations = {}
        paragraphs = text.split('\n')
        for paragraph in paragraphs:
            for name1 in Names:
                if name1 in paragraph:
                    for name2 in Names:
                        if name2 in paragraph and name1!=name2 and (name2,name1) not in relations:
                            relations[(name1, name2)] = relations.get((name1, name2), 0) + 1

# relations= {(a,b):100, (a, c):200, (c,d)：150}
        nodes = [{'name':i, 'symbolSize': 40-Names.index(i), 'category': i } for i in Names]
        #nodes = [{'name':, 'symbolSize':, 'category'}, {},{}]
        links = []
        for item in relations.keys():
            links.append({'source': item[0], 'target': item[1]})

        categories = [{'name': i} for i in Names]

        G = (
            Graph(init_opts=opts.InitOpts(width='900px', height='900px'))
            .add(
                series_name='',
                nodes=nodes,
                links=links,
                categories=categories,
                repulsion=8000,
                layout='force',#也可以'circular'
                linestyle_opts=opts.LineStyleOpts(color='source', curve=0.3, opacity=0.7)
            )
        )

        st_pyecharts(G, height='600px')