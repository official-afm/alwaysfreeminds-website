import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'AlwaysFreeMinds - Stories of Resilience & Redemption'
    }
  },
  {
    path: '/blog',
    name: 'Blog',
    component: () => import('../views/Blog.vue'),
    meta: {
      title: 'Blog - AlwaysFreeMinds'
    }
  },
  {
    path: '/blog/:slug',
    name: 'BlogPost',
    component: () => import('../views/BlogPost.vue'),
    meta: {
      title: 'Blog Post - AlwaysFreeMinds'
    }
  },
  {
    path: '/books',
    name: 'Books',
    component: () => import('../views/Books.vue'),
    meta: {
      title: 'Books - AlwaysFreeMinds'
    }
  },
  {
    path: '/consulting',
    name: 'Consulting',
    component: () => import('../views/Consulting.vue'),
    meta: {
      title: 'Consulting - AlwaysFreeMinds'
    }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
    meta: {
      title: 'About - AlwaysFreeMinds'
    }
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../views/Contact.vue'),
    meta: {
      title: 'Contact - AlwaysFreeMinds'
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue'),
    meta: {
      title: 'Page Not Found - AlwaysFreeMinds'
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// Update page title on route change
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'AlwaysFreeMinds'
  next()
})

export default router