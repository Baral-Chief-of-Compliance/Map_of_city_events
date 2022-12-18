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

function format_date(date) {
    let arr = date.slice(0, 10).split('-')
    let new_date = `${arr[2]}.${arr[1]}.${arr[0]}`

    return new_date
}

</script>

<template>
    <div class="content">
        <div class="row" v-for="event in events" v-bind:key="event.id">
            <img v-if="event.name === 'Фестиваль водных видов спорта'" :key="event.id"
                :src="'http://127.0.0.1:8000/media/' + event.eventimgSet[0].img" />

            <div v-if="event.name === 'Фестиваль водных видов спорта'" class="info">
                <div class="title">{{ event.name }}</div>
                <div class="date">{{ format_date(event.dtOfStart) }}</div>
                <div class="adress">{{ event.street }} {{ event.house }} {{ event.frame }}</div>
            </div>

        </div>
    </div>
</template>

<style scoped>
.content {
    margin-right: 180px;
    margin-left: 180px;
}

img {
    display: block;
    max-width: 300px;
    max-height: 300px;
    width: auto;
    height: auto;
    padding: 20px;
}

.row {
    margin-top: 30px;
    margin-bottom: 30px;
    display: flex;
    margin-right: 20px;
    flex-direction: row;
    box-shadow:
        6px 6px 6px -1px #e9e9e9,
        -6px 6px 6px -1px #e9e9e9;
}

.info {
    display: flex;
    flex-direction: row;
    font-size: 24px;
    margin-top: 50px;
}

.title {
    margin-left: 150px;
    margin-right: 75px;
    font-weight: bold;
}

.date {
    margin-left: 75px;
    margin-right: 75px;
}

.adress {
    margin-left: 75px;
}
</style>