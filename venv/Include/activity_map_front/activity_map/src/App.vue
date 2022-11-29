<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed, watch} from '@vue/runtime-core';
import Header from './components/Header.vue';
import NavBar from './components/NavBar.vue';


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

watch(() => {
  console.log(events.value)
})

</script>

<template>
  <Header />
  <NavBar />




  <RouterView />
</template>

<style scoped>

</style>
