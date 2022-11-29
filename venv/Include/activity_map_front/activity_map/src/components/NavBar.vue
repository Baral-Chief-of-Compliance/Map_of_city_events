<script setup>

</script>

<template>
    <div class="container">

        <div class="links">
            <router-link class="first" to="/">АФИША</router-link>
            <router-link class="second" to="/categories">КАТЕГОРИИ</router-link>
            <router-link class="third" to="/map">КАРТА</router-link>
            <router-link class="fourth" to="/archive">АРХИВ МЕРОПРИЯТИЙ</router-link>
        </div>

    </div>
</template>

<style scoped>
    .containet{
        height: 90px;
    }

    .links{
        margin-left: 500px;
        font-size: 20px;
        font-weight: medium;

    }

    .links a{
        text-decoration: none;
        color: #000000;
    }

    .links a:hover{
        color: #02C0B8;
    }

    .firs{
        margin-right: 70px;
    }

    .second{
        margin-left: 71px;
        margin-right: 71px;
    }

    .third{
        margin-left: 70px;
        margin-right: 70px;
    }

    .fourth{
        margin-left: 71px;
    }

</style>