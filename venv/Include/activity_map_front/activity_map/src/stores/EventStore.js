import { defineStore } from 'pinia'

export const useEventStore = defineStore("eventStore", {
    state: () => ({
       events: [
            {
                id: 1,
                name: 'нахуй'
            },
            {
                id: 2,
                name: 'пошел'
            }
       ] 
    })
})