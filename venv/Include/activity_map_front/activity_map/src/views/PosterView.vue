<script setup>
import { useEventStore } from '../stores/EventStore'
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

function format_date(date) {
  let arr = date.slice(0, 10).split('-')
  let new_date = `${arr[2]}.${arr[1]}.${arr[0]}`

  return new_date
}

</script>

<template>
  <div class="content">
    <div class="block" v-for="event in events" v-bind:key="event.id">
      <div class="inf">
        <div class="title"> {{ event.name }} </div>
        <div class="date"> {{ format_date(event.dtOfStart) }}</div>
      </div>
      <img :key="event.id" :src="'http://127.0.0.1:8000/media/' + event.eventimgSet[0].img" />
    </div>

    <!-- <img v-for="event in events" :key="event.id" :src="'http://127.0.0.1:8000/media/'+event.eventimgSet[0].img" /> -->
  </div>



</template>

<style scoped>
.content {
  margin-top: 45px;
  margin-bottom: 45px;
  margin-left: 100px;
  /* margin-right: 100px; */
  display: flex;
  flex-direction: row;
  overflow: hidden;
  flex-wrap: wrap;
}

.block {
  width: 400px;
  height: 250px;
  margin-bottom: 50px;
  margin-left: 90px;
  margin-right: 90px;
  position: relative;

}

.title {
  padding-top: 86px;
  text-shadow: 5px 4px 4px rgba(0, 0, 0, 0.75);
}

.date {
  padding-top: 13px;
  text-shadow: 5px 4px 4px rgba(0, 0, 0, 0.75);
  padding-bottom: 74px;
}

.block img {
  width: 400px;
  height: 250px;

}

.inf {
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  font-size: 32px;
  color: #FFFFFF;
  font-weight: bold;
  text-align: center;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
}
</style>