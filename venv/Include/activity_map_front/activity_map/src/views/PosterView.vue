<template>
    <h1>Афиша</h1>
    {{ events.name }}
 
</template>

<script setup>

const props = defineProps({
    events: {
        type: Object,
        required: true,
        default: () => {}
    }
})
</script>

<style>

</style>