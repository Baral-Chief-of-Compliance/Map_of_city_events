<script setup>
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed } from '@vue/runtime-core';
import Map from '../components/Map.vue'
import {ref} from 'vue'

const ALL_EVENTS_QUERY = gql`
  query{
    allEvents {
      id
      name
      dtOfStart
      dtOfEnd
      street
      house
      frame
      description
      url
      organizers
      latitude
      longitude
      town
      paid
      price
      ageLimit
      county
      category
      eventimgSet{
        img
      }
    }
  }
`;



const { result } = useQuery(ALL_EVENTS_QUERY)
const events = computed(() => result.value?.allEvents ?? [])
const show_city = ref(false)
const show_county = ref(false)
const show_type = ref(false)


function format_date(date) {
    let arr = date.slice(0, 10).split('-')
    let new_date = `${arr[2]}.${arr[1]}.${arr[0]}`

    return new_date
}


</script>
    
<template>

    <div  onmousedown="return true" class="content">

        <div class="search-block">
            <div class="row">
                <input class="search-in" v-model="search" placeholder="ПОИСК" />
                <div class="filter">
                    <div class="filter-content">
                        <div>
                            <img class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                        </div>
                        <div class="filter-name">
                            ДАТА
                        </div>
                    </div>

                </div>
            </div>
            <div class="row">

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
                <div  @click="show_type = !show_type" class="filter-down" id="type">
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
            
        </div>
        <button class="accept_filter" @click="show_events">
            <div class="accept-name"> 
                ПРИМЕНИТЬ ФИЛЬТРЫ
            </div>
        </button>
        <div class ='row-results'>
            <div class="block" v-for="event in events" v-bind:key="event.id">
                <img  class="img-event" v-show="event.name != 'Фестиваль водных видов спорта'" :key="event.id"
                :src="'http://127.0.0.1:8000/media/' + event.eventimgSet[0].img" />

                <div v-if="event.name != 'Фестиваль водных видов спорта'" class="info">
                    <div class="title">{{ event.name }}</div>
                    <div class="date">{{ format_date(event.dtOfStart) }}</div>
                    <div class="adress">{{ event.street }} {{ event.house }} {{ event.frame }}</div>
                </div>
            </div>
        </div>



    </div>

        <Map :events="events" />



        <!-- <div class="map">
            <yandex-map  :coords='[68.970360, 33.074172]' :zoom="11" >
                <ymap-marker v-for="event in events" :key="event.id"
                    :marker-id="event.id" 
                    :coords="[event.latitude, event.longitude]" 
                    marker-type="placemark"
                    :balloon="{header: event.name}"
                    :icon="{ color: 'red' }"                    
                    ></ymap-marker>
            </yandex-map>
        </div> -->

    </div>


</template>

<script>

    export default{
        data(){
            return {
                town_list: ["Все города"],
                county_list: ["Выбрать все"],
                type_list: ["Выбрать все"],
            }
        },

        methods: {
            show_events(){
                let names = []

                this.events.forEach(function(item){
                    names.push(item.name)
                })

                alert(names)
            }
        }
    }
</script>


<style scoped>
.content {
    margin-left: 213px;
    margin-right: 180px;
    display: flex;
    flex-direction: row;
}

.ymap-container {
    width: 780px;
    height: 554px;
}

.search-block {
    width: 780px;
}

.row {
    padding-top: 45px;
    display: flex;
    flex-direction: row;
}

.row input {
    margin-right: 45px;
}

.search-in {
    width: 250px;
    height: 50px;
    border: 3px solid #02C0B8;
    padding-left: 20px;
    color: #696969;
    background-color: #F3F3F3;
    font-size: 16px;
    font-weight: bold;

}

.filter {
    width: 250px;
    height: 50px;
    background-color: #02C0B8;
}

.filter-name {
    color: #FFFFFF;
    font-weight: bold;
    font-size: 16px;
    padding-top: 15px;
}

.filter-content{
    display: flex;
    flex-direction: row;
    margin-left: 85px;
}

.arrow_down{
    margin-top: 19px;
    margin-right: 5px;
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

.varinats{
    display: flex;
    flex-direction: column;
    margin-top: 5px;
}

.varinats_second{
    margin-top: 5px;
    margin-left: 22px;
    display: flex;
    flex-direction: column;
}

.varinats_second div{ 
    margin-top: 2px;
    margin-bottom: 2px;
    width: 160px;
}

.varinats_second div:hover{
    background-color: #CFF8F6;

}
.varinats div{
    margin-top: 2px;
    margin-bottom: 2px;
    width: 160px;
}
.varinats div:hover{
    background-color: #CFF8F6;

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

.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.img-event{
    width: 300px;
    height: 150px;
    object-fit: cover;
	object-position: 50% 50%;
}

.block{
    display: flex;
    flex-direction: row;
    margin-top: 10px;
    margin-bottom: 15px;
    box-shadow:
        6px 6px 6px -1px #e9e9e9,
        -6px 6px 6px -1px #e9e9e9;
    margin-right: 100px;
    

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

.row-results{
    padding-top: 20px;
}

.accept_filter{
    margin-top: 50px;
    width: 570px;
    height: 50px;
    background-color: #02C0B8;
    border: #02C0B8;
    cursor: pointer;
}

.accept-name{
    color: #FFFFFF;
    font-weight: bold;
    font-size: 16px;
}

</style>