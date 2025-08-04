import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    isAuthenticated: false,
    blogPosts: [],
    loading: false,
    error: null
  },
  getters: {
    isLoggedIn: state => !!state.user,
    featuredPosts: state => state.blogPosts.filter(post => post.featured),
    getPostBySlug: state => slug => state.blogPosts.find(post => post.slug === slug)
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user
      state.isAuthenticated = !!user
    },
    SET_BLOG_POSTS(state, posts) {
      state.blogPosts = posts
    },
    ADD_BLOG_POST(state, post) {
      state.blogPosts.unshift(post)
    },
    SET_LOADING(state, status) {
      state.loading = status
    },
    SET_ERROR(state, error) {
      state.error = error
    },
    CLEAR_ERROR(state) {
      state.error = null
    }
  },
  actions: {
    async fetchBlogPosts({ commit }) {
      commit('SET_LOADING', true)
      try {
        // This will be replaced with actual API call
        const mockPosts = [
          {
            id: 1,
            title: "Finding Purpose After Prison",
            slug: "finding-purpose-after-prison",
            excerpt: "How I discovered my calling and built a meaningful life after serving four years.",
            content: "Full blog post content here...",
            category: "Personal Growth",
            author: "Your Name",
            publishedAt: "2024-01-15",
            featured: true,
            image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop"
          },
          // Add more mock posts as needed
        ]
        commit('SET_BLOG_POSTS', mockPosts)
      } catch (error) {
        commit('SET_ERROR', error.message)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    
    async login({ commit }, credentials) {
      commit('SET_LOADING', true)
      try {
        // Replace with actual authentication logic
        const user = { id: 1, name: 'Admin', email: credentials.email }
        commit('SET_USER', user)
        return user
      } catch (error) {
        commit('SET_ERROR', error.message)
        throw error
      } finally {
        commit('SET_LOADING', false)
      }
    },
    
    logout({ commit }) {
      commit('SET_USER', null)
    }
  }
})