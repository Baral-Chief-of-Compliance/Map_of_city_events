<script setup>
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed } from '@vue/runtime-core';

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
                <input v-model="search" placeholder="Я хочу найти"/>
                <div>
                    ФИЛЬТР "ГОРОД"
                </div>
            </div>
            <div class="row">
                <input v-model="search" type="date"/>
                <div>
                    КАТЕГОРИИ
                </div>
            </div>

        </div>

        <div class="map">
            <yandex-map  :coords='[68.970360, 33.074172]' :zoom="11">
                <ymap-marker v-for="event in events" :key="event.id"
                    :marker-id="event.id" 
                    :coords="[event.latitude, event.longitude]" 
                    marker-type="placemark"
                    :balloon="{header: event.name}"
                    :icon="{ color: 'red' }"
                    
                    ></ymap-marker>
            </yandex-map>
        </div>

    </div>


</template>

<style scoped>
.content {
    margin-left: 180px;
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

.row{
    padding-top: 45px;
    display: flex;
    flex-direction: row;
}

.row input{
    margin-right: 45px;
}
</style>