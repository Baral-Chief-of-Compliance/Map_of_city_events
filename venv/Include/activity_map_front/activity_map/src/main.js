import { createApp, provide, h } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { createMetaManager} from 'vue-meta'
import router from './router'
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'
import ymapPlugin  from 'vue-yandex-maps'

import './assets/main.css'


const httpLink = createHttpLink({
    // You should use an absolute URL here
    uri: 'http://127.0.0.1:8000/graphql/',
  })
  
  // Cache implementation
const cache = new InMemoryCache()
  
  // Create the apollo client
const apolloClient = new ApolloClient({
    link: httpLink,
    cache,
})



const app = createApp({
    setup () {
      provide(DefaultApolloClient, apolloClient)
    },
  
    render: () => h(App),
  })

app.use(router)
app.use(createMetaManager())
app.use(createPinia())
app.use(ymapPlugin)


app.mount('#app')
