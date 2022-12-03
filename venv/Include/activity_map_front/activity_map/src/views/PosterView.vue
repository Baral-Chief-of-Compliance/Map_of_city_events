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

</script>

<template>
  <div class="content">
    <div class="block" v-for="event in events" :key="event.id"> {{ event.name }} {{ event.eventimgSet[0].img }} </div>
    <img v-for="event in events" :key="event.id" v-bind:src="require(`@/${event.eventimgSet[0].img}`)" />
    <img src="@/Мафия/29e4d32f752c6f700e41fe59123283f12e03c136.jpg" />
  </div>



</template>

<style scoped>
.content {
  margin-top: 45px;
  margin-bottom: 45px;
  padding-left: 100px;
  padding-right: 100px;
  display: flex;
  flex-direction: row;
}

.block {
  width: 400px;
  height: 250px;
  margin-bottom: 50px;
  margin-left: 90px;
  margin-right: 90px;
  border: 1px solid;
}
</style>