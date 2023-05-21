import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CategoriesView from '../views/CategoriesView.vue'
import MapView from '../views/MapView.vue'
import ArchiveView from '../views/ArchiveView.vue'
import PosterView from '../views/PosterView.vue'
import EventInfo from '../views/EventInfo.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'poster',
      component: PosterView,
      props: true,
      meta: {
        title: 'АФИША'
      }
    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },

    {
      path: '/categories',
      name: 'categories',
      component: CategoriesView,
      meta: {
        title: 'КАТЕГОРИИ'
      }

    },

    {
      path: '/map',
      name: 'map',
      component: MapView,
      meta: {
        title: 'КАРТА'
      }
    },

    {
      path: '/archive',
      name: 'archive',
      component: ArchiveView,
      meta: {
        title: 'АРХИВ МЕРОПРИЯТИЙ'
      }
    },
    {
      path: '/events/:id',
      name: 'events',
      component: EventInfo,
      meta:{
        title: 'Иноформация о мероприятии'
      }
    }
  ]
});

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title}`;
  next();
})

export default router
