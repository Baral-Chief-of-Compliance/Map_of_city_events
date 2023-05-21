import { defineStore } from 'pinia'

export const useEventStore = defineStore("eventStore", {
    state: () => ({
       events: []
    }),

    actions: {
        addEvent(event){
            this.events.push(event)
        }
    }
})