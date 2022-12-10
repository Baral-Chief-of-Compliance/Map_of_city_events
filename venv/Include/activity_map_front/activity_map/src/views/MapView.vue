<script setup>
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed } from '@vue/runtime-core';
import Map from '../components/Map.vue'

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
      eventimgSet{
        img
      }
    }
  }
`;



const { result } = useQuery(ALL_EVENTS_QUERY)
const events = computed(() => result.value?.allEvents ?? [])

</script>
    
<template>

    <div class="content">

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

                <div class="filter-down" id="city">
                    <div class="filter-down-content">
                        <div>
                            <img class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                        </div>
                        <div class="filter-down-name"> 
                            ГОРОД
                        </div>
                    </div>
                </div>

                <div class="filter-down" id="county">
                    <div class="filter-down-content">
                        <div>
                            <img class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                        </div>
                        <div class="filter-down-name"> 
                            ОКРУГ
                        </div>
                    </div>
                </div>

                <div class="filter-down" id="type">
                    <div class="filter-down-content">
                        <div>
                            <img class="arrow_down" src="../assets/map/Line_down.svg" width="20" height="12" alt="image format png" />
                        </div>
                        <div class="filter-down-name"> 
                            ТИП
                        </div>
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
</style>