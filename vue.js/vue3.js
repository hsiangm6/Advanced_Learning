//官方教學:https://book.vue.tw/CH1/1-1-introduction.html

//Hello Vue!
const vm = Vue.createApp({
    //template: `<div>{{message}}好棒</div>`, 
    //template模板屬性:會將template內的html當作模板使用，顯示效果和直接使用html模板是一樣的
    data() {
        return {
            message: 'Hello Vue 3.0!',
            price: 100,
            quantity: 10
        }
    },
    methods: { //在實體裡加上函式
        subtotalMethods() { //function
            return this.price * this.quantity;
        }
    },
    computed: { //會將計算後的結果暫存，若它所觀察到的屬性(this.XXX)沒有被更新的情況下，computed就不會被重複執行
        //computed中的function無法帶入和使用參數
        //related web:https://book.vue.tw/CH1/1-3-computed-and-methods.html
        subtotalComputed() {
            return this.price * this.quantity;
        }
    }
}).mount('#app');

//小心data共用帶來的汙染:https://book.vue.tw/CH1/1-2-instance.html
vm.$data.message = '30cm';

const dataObj = {
    name: 'qwer'
}

const vm1 = Vue.createApp({
    data() {
        return { ...dataObj } //
    },
}).mount('#app1');

const vm2 = Vue.createApp({
    data() {
        return { ...dataObj }
    }
}).mount('#app2');

vm1.$data.name = 'hello hello';

//幣值轉換
const curr_methods = Vue.createApp({
    data() {
        return {
            twd: 0.278, //台幣
            jpy: 1, //日幣
        }
    },
    methods: {
        twd2jpy() {
            this.jpy = Number.parseFloat(Number(this.twd) / 0.278).toFixed(3);
        },
        jpy2twd() {
            this.twd = Number.parseFloat(Number(this.jpy) * 0.278).toFixed(3);
        },
    }
}).mount('#curr_methods');

const curr_computed = Vue.createApp({
    data() {
        return {
            twd: 0.278 //不管幣值如何換算，只需要一種基準值
        }
    },
    computed: {
        jpy: {
            get() { //twd to jpy(對twd做加工計算) //將另一個實體屬性加工後回傳
                return Number.parseFloat(Number(this.twd) / 0.278).toFixed(3);
                //toFixed():將一個數字轉換成一個固定小數位數的字符串
            },
            set(val) { //jpy to twd(在jpy更新時，回去改寫twd) //修改對應的computed屬性，如果沒有加上set()，則不允許手動修改對應的computed屬性
                this.twd = Number.parseFloat(Number(val) * 0.278).toFixed(3);
            }
        },
        used: {
            get() {
                return Number.parseFloat(Number(this.twd) / 28.540).toFixed(3);
            },
            set() {
                this.twd = Number.parseFloat(Number(val) * 28.540).toFixed(3);
            },
        }
    }
}).mount('#curr_computed');

//官方教學:https://book.vue.tw/CH1/1-4-directive.html
//v-bind:由vue.js控制標籤的屬性(ex:id, src, href)
const attr = Vue.createApp({
    data() {
        return {
            customId: 'item-id-1'
        }
    }
}).mount('#attr');

//v-model:表單綁定
const binding = Vue.createApp({
    data() {
        return {
            message: 'Hello', //input, textarea
            picked: 1, //單選框
            checkedNames: [], //多選框:因為是複選，所以必須是陣列
            selected: '',
        }
    }
}).mount('#binding');

const model_binding = Vue.createApp({
    data() {
        return {
            rawContent: '<h5>HELLO Vue!</h5>'
        }
    }
}).mount('#model-binding');

const css_binding = Vue.createApp({
    data() {
        return {
            message: ''
        }
    },
    //操作style屬性
    computed: {
        isValid() {
            return this.message.length <= 10;
        },
        msgStyle() {
            return {
                'border': this.isValid ? '' : 'red solid 1px',
                'color': this.isValid ? '' : 'red'
            };
        }
    }
}).mount('#css-binding');

//事件處理:https://book.vue.tw/CH1/1-5-events.html
const event_binding = Vue.createApp({
    data() {
        return {
            amount: 0,
            count: 0
        }
    },
    methods: {
        plus(amount, event) {
            this.count++;
            console.log(event.target.tagName);
            this.count += amount
        }
    },
}).mount('#event-binding');

const loop = Vue.createApp({
    data() {
        return {
            //物件本身不帶有順序，如果要確保渲染順序，可先將物件轉換為陣列後再排序
            arr: ['008', 'JS', 'is', 'awesome'],
            book: {
                title: 'o8js',
                author: 'Kuro',
                publishedAt: '2019/09',
            },
            lists: [
                {
                    id: 'task001',
                    title: 'choose 1',
                    isDone: false
                },
                {
                    id: 'task002',
                    title: 'choose 2',
                    isDone: false
                },
                {
                    id: 'task003',
                    title: 'choose 3',
                    isDone: false
                },

            ]
        }
    },
    computed: {
        todoLists() {
            return this.lists.filter(d => !d.isDone)
        },
        doneLists() {
            return this.lists.filter(d => d.isDone)
        }
    }
}).mount('#loop');

//元件的生命週期與更新:https://book.vue.tw/CH1/1-7-lifecycle.html
const renew_and_sync = Vue.createApp({
    data() {
        return {
            msg: '',
            messages: ['Hello', 'Vue.js', 'good'],
            scrollHeight: 0,
            realScrollHeight: 0
        }
    },
    watch: {
        //當this.msg被更新時被觸發
        msg(val, oldValue) {
            console.log('new:${val}');
            console.log('old: ${oldValue}');
        }
    },
    methods: {
        addToMessages() {
            this.messages.push(this.msg);
            this.msg = '';

            //要在訊息增加時，訊息列表的卷軸自動捲至最底
            //等待畫面更新後再即時抓取元素屬性，
            //     否則執行到 el.scrollTop = el.scrollHeight 的時候，畫面還未更新
            //透過vue.js的$nextTick可以確保裡面callback function執行的任務會等更新結束後才執行
            this.$nextTick(() => {
                //透過this.$el取得實體綁定後的DOM
                const el = document.querySelector('.messages');
                //將el.scrollTop指定為卷軸的高度el.scrollHeight
                el.scrollTop = el.scrollHeight;
                this.realScrollHeight = el.scrollHeight;
                this.scrollHeight = el.scrollHeight;
            })

        }
    }
}).mount('#renew-and-sync')


//元件系統的特性:https://book.vue.tw/CH2/2-1-components.html
const compo = Vue.createApp({
    data() {
        return {
            count: 0
        }
    },
    //若環境支援 ES Module 也可透過 import 的方式將外部檔案引入子元件:
    //import myComponent from './components/my-component.js';
    components: { //區域型
        'my-component': {
            //子元件的options
            template: `<div>Hello Vue!!!</div>`,
        }
    },
    //想保留data屬性的初始狀態，又不希望引用全域變數造成data共用的汙染，
    //  可透過Object.assign與this.$options.data()重新指定元件內的data的內容，
    //  讓它回復初始狀態
    methods: {
        resetData() {
            Object.assign(this.$data, this.$option.data());
        }
    }
});
// 子元件
compo.component('child-comp', { //全域型
    template: `
      <div class="app-child">
        <div>Hello Vue!</div>
      </div>`
});
compo.mount('#compo');

//元件之間的溝通傳遞
// Props屬性:引用外部狀態
const quote_props = Vue.createApp({
    data() {
        return {
            msg: '這是外層元件的msg'
        }
    }
}).component('my-component-props', {
    template: `
        <div class="component">
            <div>從props來的parentMsg==>{{parentMsg}}</div>
            <div>自己的msg==>{{msg}}</div>
        </div>
    `,
    props: ["parentMsg"],
    props: {
        'props-number': { //若傳遞float會有error
            type: [String, Number],
            required: true, //指定props為必要的屬性
            default: 'Hello', //為props指定預設值

        }
    },
    data() {
        return {
            msg: '這是子元件的msg'
        }
    }
}).mount('#quote-props')



