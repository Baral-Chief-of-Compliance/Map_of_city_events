<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { computed, watchEffect} from '@vue/runtime-core';
import Header from './components/Header.vue';
import NavBar from './components/NavBar.vue';
import  Footer from './components/Footer.vue';
import { useEventStore } from './stores/EventStore';


const eventStore = useEventStore()

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

let a = 42

watchEffect(() => {
  console.log(events.value)
})


</script>

<template>
  <metainfo>
    <template v-slot:title="{ content }">{{ content ? `${content} | SITE_NAME` : `SITE_NAME` }}</template>
  </metainfo>
  <Header />
  <NavBar />
  <RouterView />
  <Footer />
</template>



<style scoped>

</style>
