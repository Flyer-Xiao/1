import streamlit as st
from PIL import Image

##添加侧边栏
page = st.sidebar.radio('我的首页',['主页','我的图片处理工具','我的智能词典','我的留言区'])

# with open('misic.wav','rb') as f:             #添加声音
#     music = f.read()
#     st.audio(music)

# a = 'green['电影推荐']'                         #添加文字（带颜色）
# st.write(a)
# st.image('黑幕.jpg')                          #添加图片
# st.video('视频.mp4')                          #添加视频

def page_2():
    '''我的图片处理工具'''
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))

def page3():
    '''我的智慧词典'''
    st.write('我的智慧词典')
    #读取本地文件并保存至word_list
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list = f.read().split('\n')

    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')

    #将列表中的内容导入字典，方便查询，格式为“单词:编号、解释”
    word_dict = {}
    for i in word_list:
        word_dict[i[1]] = [int(i[0]),i[2]]
        
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}

    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('请输入要查询的单词:')
    
    if word in word_dict:
        st.write(word_dict[word])
        n = word_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8')as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数',times_dict[n])

def page4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')

    for i in message_list:
        if i[1] == '阿短':
            with st.chat_message(''):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message(''):
                st.write(i[1],':',i[2])

    name = st.selectbox('我是...',['阿短','编程猫'])
    new_messang = st.text_input('想要说的话')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1),name,new_messang])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

    


def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()

    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (g,b,r)
    return img


    
if page == '主页':
    a = ":green[Welcome to Chemistry World!]"
    st.write(a)
    st.image('化学.png') 
    
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page3()
elif page == '我的留言区':
    page4()

    

