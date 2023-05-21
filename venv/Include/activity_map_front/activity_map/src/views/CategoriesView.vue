<template>
    <div class="content">
        <div class="row-filter">

        <div>
            <div @click="show_city = !show_city" class="filter-down" id="city">
                <div class="filter-down-content">
                    <div>
                        <Transition>
                            <div>
                                <img  v-show="!show_city" class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                                <img  v-show="show_city" class="arrow_down" src="../assets/map/Line_up.svg" width="20" height="12" alt="image format png" />
                            </div>
                        </Transition>
                    </div>
                    <div class="filter-down-name"> 
                        ГОРОД
                    </div>
                </div>
            </div>
            <Transition>
                    <div class='varinats' v-show="show_city" >
                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Все города" v-model="town_list">
                                <span class="check__box"></span>
                                Все города
                            </label>
                        </div>
                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Мурманск" v-model="town_list">
                                <span class="check__box"></span>
                                Мурманск
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Мончегорск" v-model="town_list">
                                <span class="check__box"></span>
                                Мончегорск
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Полярные Зори" v-model="town_list">
                                <span class="check__box"></span>
                                Полярные Зори
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Оленегорск" v-model="town_list">
                                <span class="check__box"></span>
                                Оленегорск
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Кировск" v-model="town_list">
                                <span class="check__box"></span>
                                Кировск
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Апатиты" v-model="town_list">
                                <span class="check__box"></span>
                                Апатиты
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Гаджиево" v-model="town_list">
                                <span class="check__box"></span>
                                Гаджиево
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Заозёрск" v-model="town_list">
                                <span class="check__box"></span>
                                Заозёрск
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Кандалакша" v-model="town_list">
                                <span class="check__box"></span>
                                Кандалакша
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Кола" v-model="town_list">
                                <span class="check__box"></span>
                                Кола
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Островной" v-model="town_list">
                                <span class="check__box"></span>
                                Островной
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Полярный" v-model="town_list">
                                <span class="check__box"></span>
                                Полярный
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Североморск" v-model="town_list">
                                <span class="check__box"></span>
                                Североморск
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Снежногорск" v-model="town_list">
                                <span class="check__box"></span>
                                Снежногорск
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Заполярный" v-model="town_list">
                                <span class="check__box"></span>
                                Заполярный
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Ковдор" v-model="town_list">
                                <span class="check__box"></span>
                                Ковдор
                            </label>
                        </div>

                        
                    </div>
            </Transition>
            </div>

            <div>
                <div  @click="show_county = !show_county"  class="filter-down" id="county">
                    <div class="filter-down-content">
                        <div>
                            <Transition>
                                <div>
                                    <img  v-show="!show_county" class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                                    <img  v-show="show_county" class="arrow_down" src="../assets/map/Line_up.svg" width="20" height="12" alt="image format png" />
                                </div>
                            </Transition>
                            
                        </div>
                        <div class="filter-down-name"> 
                            ОКРУГ
                        </div>
                    </div>
                </div>
                <Transition>
                    <div class='varinats_second' v-show="show_county" >

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Выбрать все" v-model="county_list">
                                <span class="check__box"></span>
                                Выбрать все
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Первомайский" v-model="county_list"> 
                                <span class="check__box"></span>
                                Первомайский
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Октябрьский" v-model="county_list">
                                <span class="check__box"></span>
                                Октябрьский
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Ленинский" v-model="county_list">
                                <span class="check__box"></span>
                                Ленинский 
                            </label>
                        </div>

                    </div>
                </Transition>
            
            </div>

            <div>
                <div  @click="show_type = !show_type" class="filter-down" id="county">
                    <div class="filter-down-content">
                        <div>
                            <Transition>
                                <div>
                                    <img  v-show="!show_type" class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                                    <img  v-show="show_type" class="arrow_down" src="../assets/map/Line_up.svg" width="20" height="12" alt="image format png" />
                                </div>
                            </Transition>
                        </div>
                        <div class="filter-down-name"> 
                            ТИП
                        </div>
                    </div>
                </div>

                <Transition>
                    <div class='varinats_second' v-show="show_type" >
                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Выбрать все" v-model="type_list">
                                <span class="check__box"></span>
                                Выбрать все
                            </label>
                        </div>
                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Концерт" v-model="type_list">
                                <span class="check__box"></span>
                                Концерт
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Фестиваль" v-model="type_list">
                                <span class="check__box"></span>
                                Фестиваль
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Развлечение" v-model="type_list">
                                <span class="check__box"></span>
                                Развлечение
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Тренинг" v-model="type_list">
                                <span class="check__box"></span>
                                Тренинг
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Выставка" v-model="type_list">
                                <span class="check__box"></span>
                                Выставка
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Квест" v-model="type_list">
                                <span class="check__box"></span>
                                Квест
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Другое" v-model="type_list">
                                <span class="check__box"></span>
                                Другое
                            </label>
                        </div>

                    </div>
                </Transition>
            
            </div>

            <div>
                <div  @click="show_age = !show_age" class="filter-down" id="county">
                    <div class="filter-down-content">
                        <div>
                            <Transition>
                                <div>
                                    <img  v-show="!show_age" class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                                    <img  v-show="show_age" class="arrow_down" src="../assets/map/Line_up.svg" width="20" height="12" alt="image format png" />
                                </div>
                            </Transition>
                        </div>
                        <div class="filter-down-name"> 
                             ВОЗРАСТ
                        </div>
                    </div>
                </div>

                <Transition>
                    <div class='varinats_second' v-show="show_age" >
                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="Выбрать все" v-model="age_limit_list">
                                <span class="check__box"></span>
                                Выбрать все
                            </label>
                        </div>
                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="0+" v-model="age_limit_list">
                                <span class="check__box"></span>
                                0+
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="6+" v-model="age_limit_list">
                                <span class="check__box"></span>
                                6+
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="12+" v-model="age_limit_list">
                                <span class="check__box"></span>
                                12+
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="14+" v-model="age_limit_list">
                                <span class="check__box"></span>
                                14+
                            </label>
                        </div>


                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="16+" v-model="age_limit_list">
                                <span class="check__box"></span>
                                16+
                            </label>
                        </div>

                        <div>
                            <label class="check">
                                <input type="checkbox" class="check__input" value="18+" v-model="age_limit_list">
                                <span class="check__box"></span>
                                18+
                            </label>
                        </div>

                    </div>
                </Transition>
            
            </div>

            <div>
                <div  @click="show_date = !show_date" class="filter-down" id="type">
                    <div class="filter-down-content">
                        <div>
                            <Transition>
                                <div>
                                    <img  v-show="!show_date" class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                                    <img  v-show="show_date" class="arrow_down" src="../assets/map/Line_up.svg" width="20" height="12" alt="image format png" />
                                </div>
                            </Transition>
                        </div>
                        <div class="filter-down-name"> 
                             ДАТА
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <div class="row-button">
            <div class="chanel" @click="chanel">
                СБРОСИТЬ
            </div>
            <div class="accept" @click="use_filter">
                ПРИМЕНИТЬ
            </div>
        </div>

        <div class ='row-results'>
            <div class="block" v-for="event in events" v-bind:key="event.id"
            >
                <img  class="img-event"  :key="event.id"
                :src="'http://127.0.0.1:8000/' + event.img" />

                <div class="info" @click="eneter_page(event.id)">
                    <div class="title">{{ event.name }}</div>
                    <div class="date">{{ format_date(event.dt_of_start) }}</div>
                    <div class="adress">{{ event.street }} {{ event.house }} {{ event.frame }}</div>
                </div>
            </div>
        </div>

        <!-- <div class="row-search">
            <div class="block" v-for="event in events" v-bind:key="event.id">
                <img  class="img-event" v-show="event.name != 'Фестиваль водных видов спорта'" :key="event.id"
                :src="'http://127.0.0.1:8000/media/' + event.eventimgSet[0].img" />

                <div v-if="event.name != 'Фестиваль водных видов спорта'" class="info">
                    <div class="title">{{ event.name }}</div>
                    <div class="date">{{ format_date(event.dtOfStart) }}</div>
                    <div class="adress">{{ event.street }} {{ event.house }} {{ event.frame }}</div>
                </div>
            </div>
        </div> -->
    </div>
</template>


<script>
import axios from 'axios'


export default{
    data(){
        return{
            town_list: ["Все города"],
            county_list: ["Выбрать все"],
            type_list: ["Выбрать все"],
            age_limit_list: ["Выбрать все"],

            show_city: false,
            show_county: false,
            show_type: false,
            show_age: false,
            show_date: false,
            events: []
        }
    },

    methods:{
        eneter_page(id){
            this.$router.push({ name: 'events', params: {id: id}})
        },
        format_date(date) {
                let arr = date.slice(0, 10).split('-')
                let new_date = `${arr[2]}.${arr[1]}.${arr[0]}`

                return new_date
            },
        chanel(){
            this.town_list = ["Все города"],
            this.county_list = ["Выбрать все"],
            this.type_list = ["Выбрать все"],
            this.age_limit_list = ["Выбрать все"]

        },

        use_filter(){
                axios.post("http://127.0.0.1:8000/filter_events/", {
                    town_list: this.town_list,
                    county_list: this.county_list,
                    type_list: this.type_list,
                    age_limit_list: this.age_limit_list
                }).then(
                    response => (
                        this.events = response.data.events
                    )
                )
            }
    }
}
</script>


<style scoped>
    .content{
        margin-left: 460px;
        padding-top: 45px;
        display: flex;
        flex-direction: column;
    }

    .filter-down{
        width: 160px;
        height: 50px;
        background-color: #02C0B8;
    }

    .filter-down:hover{
        cursor: pointer;
    }

    .filter-down-name{
        color: #FFFFFF;
        font-weight: bold;
        font-size: 16px;
        padding-top: 15px;
    }

    .filter-down-content{
        display: flex;
        flex-direction: row;
        margin-left: 35px;
    }

    #city{
        margin-right: 23px;
    }

    #county{
        margin-left: 22px;
        margin-right: 23px;
    }

    #type{
        margin-left: 22px;
    }


    .arrow_down{
        margin-top: 19px;
        margin-right: 5px;
    }

    .check{
        padding-left: 1.2em;

    }

    .check__input{
        position: absolute;
        appearance: none;
    }
    .check:hover{
        cursor: pointer;
        background-color: #CFF8F6;
        
    }

    .check__box{
        position: absolute;
        width: 1em;
        height: 1em;
        background-image: url(../assets/checkbox/checkbox.svg);
        margin-left: -1.2em;
    }

    .check__input:checked + .check__box{
        background-image: url(../assets/checkbox/checkbox_in.svg);
    }

    .row-filter{
        display: flex;
        flex-direction: row;
    }


    .row-button{
        display: flex;
        flex-direction: row;
        margin-top: 45px;
        margin-bottom: 25px;
    }

    .chanel{
        width: 468px;
        height: 30px;
        background-color: #D9D9D9;
        text-align: center;
        padding-top: 15px;
        font-weight: bold;
        margin-right: 23px;
    }

    .accept{
        width: 468px;
        height: 30px;
        background-color: #02C0B8;
        text-align: center;
        padding-top: 15px;
        font-weight: bold;
        margin-left: 22px;
    }

    .row-search{
        margin-top: 20px;
        display: flex;
        flex-direction: row;
        overflow: hidden;
        flex-wrap: wrap;
        margin-right: 400px;
    }

    .img-event{
        width: 300px;
        height: 150px;
        object-fit: cover;
        object-position: 50% 50%;
    }

    .block{
        position: relative;
        padding-left: 15px;
        padding-right: 15px;
    }

    .title{
        font-weight: bold;
        padding-bottom: 5px;
        text-align: center;
    }

    .date{
        padding-top: 5px;
        padding-bottom: 5px;
        text-align: center;
    }

    .adress{
        padding-top: 5px;
        padding-bottom: 5px;
        text-align: center;
    }

    .varinats{
        margin-top: 5px;
    }

    .varinats_second{
        margin-top: 5px;
        margin-left: 22px;
    }

    .row-results{
        padding-top: 20px;
    }

    .block{
        display: flex;
        flex-direction: row;
        margin-top: 10px;
        margin-bottom: 15px;
        box-shadow:
            6px 6px 6px -1px #e9e9e9,
            -6px 6px 6px -1px #e9e9e9;
        margin-right: 32%;
    

    }

    .img-event{
        width: 300px;
        height: 150px;
        object-fit: cover;
        object-position: 50% 50%;
    }

    .info{
        padding-top: 20px;
        padding-left: 20px;
    }

    .title{
        font-weight: bold;
        padding-bottom: 5px;
        text-align: center;
    }

    .date{
        padding-top: 5px;
        padding-bottom: 5px;
        text-align: center;
    }

    .adress{
        padding-top: 5px;
        padding-bottom: 5px;
        text-align: center;
    }


</style>