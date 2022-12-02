<template>
    <h1>Афиша</h1>
    {{ eventStore.events }}

</template>

<script setup>
    import { useEventStore } from '../stores/EventStore'

    const eventStore = useEventStore()

</script>

<style>

</style>