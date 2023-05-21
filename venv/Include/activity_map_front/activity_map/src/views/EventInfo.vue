<template>
    <div class="content">
        <span class="label">{{ name }}</span>

        <div class="photo_and_inf">
            <div>
                <img  class="img-event"
                :src="'http://127.0.0.1:8000/' + img" />
            </div>
            <div class="inf">

                <div class="inf_row">
                    <span class="inf_row_label">
                        Дата начал: 
                    </span>
                    <span class="inf_row_back">
                        {{ dt_of_start }}
                    </span>
                </div>

                <div class="inf_row">
                    <span class="inf_row_label">
                        Дата конца: 
                    </span>
                    <span class="inf_row_back">
                        {{ dt_of_end }}
                    </span>
                </div>

                <div class="inf_row">
                    <span class="inf_row_label">
                        Категория: 
                    </span>
                    <span class="inf_row_back">
                        {{ category }}
                    </span>
                </div>

                <div class="inf_row">
                    <span class="inf_row_label">
                        Возрастное ограничение: 
                    </span>
                    <span class="inf_row_back">
                        {{ age_limit }}
                    </span>
                </div>

                <div class="inf_row">
                    <span class="inf_row_label">
                        Основа мероприятия:
                    </span>
                    <span class="inf_row_back">
                        {{ paid }}
                    </span>
                </div>

                <span class="inf_row_label_more">
                        Подробнее
                </span>
            </div>
        </div>

        <div class="description">
            <span class="description_label">
                Описание:
            </span>
            <div class="description-text">
                {{ description }}
            </div>
        </div>

        <div class="map">
            <span class="description_label">
                Местоположение:
            </span>

            <yandex-map
                :coords="[this.latitude, this.longitude]"
                :zoom="15"
            >
                <ymap-marker 
                    :coords="[this.latitude, this.longitude]" 
                    marker-id="1" 
                />
            </yandex-map>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

export default{
    data(){
        return{
            name: "",
            dt_of_start: "",
            dt_of_end: "",
            town: "",
            street: "",
            house: "",
            frame: "",
            description: "",
            url: "",
            organizers: "",
            latitude: "",
            longitude: "",
            paid: "",
            price: "",
            age_limit: "",
            county: "",
            category: "",
            img: ""
        }
    },

    methods:{

        format_date(date) {
                let arr = date.slice(0, 10).split('-')
                let new_date = `${arr[2]}.${arr[1]}.${arr[0]}`

                return new_date
        },
        
        get_inf_about_event(){
            axios.get(`http://127.0.0.1:8000/all_events/${this.$route.params.id}`)
            .then(response => {
                this.name = response.data.name,
                this.dt_of_start = this.format_date(response.data.dt_of_start),
                this.dt_of_end = this.format_date(response.data.dt_of_end),
                this.town = response.data.town,
                this.street = response.data.street ,
                this.house = response.data.house,
                this.frame = response.data.frame,
                this.description = response.data.description,
                this.url = response.data.url,
                this.organizers = response.data.organizers,
                this.latitude = response.data.latitude,
                this.longitude = response.data.longitude,
                this.paid = response.data.paid ,
                this.price = response.data.price,
                this.age_limit = response.data.age_limit,
                this.county = response.data.county,
                this.category = response.data.category,
                this.img = response.data.img
            })
        }
    },

    mounted(){
        this.get_inf_about_event()
    }
}
</script>


<style>
    .content{
        margin-top: 45px;
        margin-left: 16%;
        margin-right: 16%;
    }

    .label{
        font-size: 32px;
        font-weight: bold;
        margin-left: 28%;
        margin-bottom: 25px; 
    }

    .photo_and_inf{
        display: flex;
        flex-direction: row;
        margin-top: 25px;
    }

    .inf{
        margin-left: 125px;
    }

    .inf_row_label{
        font-weight: bold;
        font-size: 24px;
        color: #02C0B8
    }

    .inf_row{
        margin-bottom: 20px;
    }

    .inf_row_label_more{
        font-weight: bold;
        font-size: 24px;
        color: #02C0B8;
        text-decoration: underline #02C0B8;
    }

    .inf_row_back{
        font-size: 24px;
        margin-left: 15px;

    }

    .img-event{
       width: 505px;
       height: 274px; 
    }

    .description_label{
        font-weight: bold;
        font-size: 24px;
        color: #02C0B8;
    }

    .description{
        margin-top: 30px;
    }

    .map{
        margin-top: 30px;
    }

    .description-text{
        margin-top: 21px;
        font-size: 24px;
    }

    .ymap-container {
        margin-top: 34px;
        margin-bottom: 50px;
        width: 1300px;
        height: 700px;
    }
</style>


