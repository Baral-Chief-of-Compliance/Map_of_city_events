<script setup>

</script>

<template>
    <div class="container">

        <div class="links">
            <router-link class="external-left" :to="{ name: 'poster'}">АФИША</router-link>
            <router-link class="inside" to="/categories">КАТЕГОРИИ</router-link>
            <router-link class="inside" to="/map">КАРТА</router-link>
            <router-link class="external-right" to="/archive">АРХИВ МЕРОПРИЯТИЙ</router-link>
        </div>

    </div>
</template>

<style scoped>
    .container{
        height: 90px;
        background-color: #EAEEEF;
    }

    .links{
        margin-left: 500px;
        font-size: 20px;
        font-weight: medium;
        padding-top: 33px;
        padding-bottom: 33px;
    }

    .links a{
        text-decoration: none;
        color: #000000;
    }

    .links a:hover{
        color: #02C0B8;
    }

    .external-left{
        margin-right: 71px;
    }

    .inside{
        margin-left: 70px;
        margin-right: 71px;
    }

    .external-right{
        margin-left: 70px;
    }
</style>