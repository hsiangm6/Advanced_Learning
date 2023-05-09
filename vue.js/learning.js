//官方教學:https://book.vue.tw/CH1/1-1-introduction.html
//基本用法: https://ithelp.ithome.com.tw/articles/10198843
// var/let/const: https://ithelp.ithome.com.tw/m/articles/10259899
//一、綁定數據:
let firstVueObj = new Vue({
    el: '#firstVue',
    data: {
        content: 'Hello!world!',
    },
})

//二、綁定屬性
// let timeData = {
//     content:'現在時間',
//     nowTime:'目前是' + String(new Date()),
// }
// let timeDiv = new Vue({
//     el:'#timeDiv',
//     data:timeData,
// })

//三、綁定事件
let timeData = {
    content: '點我看時間',
}
let timeDiv = new Vue({
    el: '#timeDiv',
    data: timeData,
    methods: {
        getTime: () => {
            console.log(String(new Date()))
        },
    },
})

//條件判斷:https://ithelp.ithome.com.tw/articles/10198881
//文字切換
// let vueData = {
//     status: 'B',
// }
// let vueDiv = new Vue({
//     el: '#vueDiv',
//     data: vueData,
// })

//input切換
let vueData = {
    status: true,
}
let vueMethods = {
    //切換status的值
    changeStatus: () => {
        vueData.status ? vueData.status = false : vueData.status = true //if vueData.status=true, change to vueData.status=false
    }
}
let vueDiv = new Vue({
    el: '#vueDiv',
    data: vueData,
    methods: vueMethods,
})

//迴圈:https://ithelp.ithome.com.tw/articles/10198895, https://ithelp.ithome.com.tw/articles/10198895 (含陣列的異動方式)
//文字輸出
let listData = {
    //lists屬性中存著陣列
    lists: [
        //陣列中擁有多個相同key但值不一樣的物件
        { item: '學Vue.js' },
        { item: '學React' },
        { item: '學Angular2' }
    ]
}
let todoList = new Vue({
    el: '#todoList',
    data: listData,
})

//反轉陣列
let listData2 = {
    titleText: '請輸入',
    lists: [
        { id: 'name', item: '姓名' },
        { id: 'mail', item: '信箱' },
        { id: 'tel', item: '電話' }
    ]
}
let listMethods = {
    changeSort: () => {
        //反轉陣列
        listData2.lists.reverse()
    }
}
let formList = new Vue({
    el: '#formList',
    data: listData2,
    methods: listMethods,
})


//讓v-model雙向綁定抓住你的資料:https://ithelp.ithome.com.tw/articles/10198927
//input
let nameData = {
    text1: '神Q超人'
}
let name = new Vue({
    el: '#name',
    data: nameData,
})

//texarea
let introduceData = {
    text2: '你好，我是...'
}
let introduce = new Vue({
    el: '#introduce',
    data: introduceData,
})

//select, checkbox, radio
let genderData = {
    selectName: '',
    checkedNames: [], //checkbox
    radioNames: '', //radio
    //資料會存在v-for="list in lists"的list中，但實際上的data內並沒有list這個屬性，所以必須再增加一個selectName給v-model綁定數據，
    //  只要select的選項改變，list內的item就會把目前綁定的value值(html中的:value="list.item")寫給selectName
    //如果是checkbox，selectName:''要改成checkedNames : [], 因為這裡綁定的值要是陣列
    lists: [
        { val: "M", item: '男' },
        { val: "W", item: '女' },
    ]
}
let gender = new Vue({
    el: '#gender',
    data: genderData,
})

//非即時綁定:v-model.lazy
let nameData_lazy = {
    text: '神Q超人'
}
let name_lazy = new Vue({
    el: '#name_lazy',
    data: nameData_lazy,
})

//只容許數字進行綁定:v-model.number
let ageData = {
    text: '神Q超人'
}
let age = new Vue({
    el: '#age',
    data: ageData,
})

//綁定資料的時候自動清除前後的空白
let nameData_trim = {
    text: '神Q超人'
}
let name_trim = new Vue({
    el: '#name_trim',
    data: nameData_trim,
})


//計算屬性(computed):需要先處理再綁定的資料，可以直接把處理資料的邏輯寫在計算屬性中
let textData = {
    text: 'Hello!World!'
}

let showText = new Vue({
    el: '#baseVue',
    data: textData,
    computed: {
        //在computed中創建一個reText屬性來放剛剛的表達式
        reText: function () {
            /*這裡的this指向showText這個實體
            可以從實體物件去取我們放在data中的資料
            也可以直接透過textData去取值*/
            return this.text.split('').reverse().join('')
        }
    }
})


//watch:表單上的值發生改變的時候，去執行某些事件
//例如判斷輸入資料的格式正不正確
//資料
let nameData_correct = {
    name_correct: 'Tom Cruise',
    alertMessage: '',
}
//方法
let nameMethod = {
    //檢查姓名格式
    checkName: () => {
        let newName = document.getElementById('name_correct').value
        if (newName.trim().indexOf(' ') == -1) {
            //trim() 方法會移除字串起始及結尾處的空白字元, indexOf() 方法會回傳給定元素於陣列中第一個被找到之索引，若不存在於陣列中則回傳-1
            nameData.alertMessage = '請輸入正確的姓名格式'
        }
        else
            nameData.alertMessage = ''
    }
}
let nameVue = new Vue({
    el: '#nameVue',
    data: nameData_correct,
    methods: nameMethod,
})
