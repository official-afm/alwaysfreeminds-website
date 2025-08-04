<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-primary-900 via-primary-800 to-primary-600 text-white py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-6">Stories That Matter</h1>
        <p class="text-xl text-gray-200">
          Real experiences, practical insights, and hope for anyone ready to transform their life.
        </p>
      </div>
    </section>

    <!-- Search and Filter -->
    <section class="py-8 bg-gray-50 border-b">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between space-y-4 md:space-y-0">
          <!-- Search -->
          <div class="relative max-w-md w-full">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search stories..."
              class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            >
            <svg class="absolute left-3 top-2.5 h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
            </svg>
          </div>

          <!-- Category Filter -->
          <div class="flex space-x-2">
            <button
              v-for="category in categories"
              :key="category"
              @click="selectedCategory = category"
              :class="[
                'px-4 py-2 rounded-lg text-sm font-medium transition-colors duration-200',
                selectedCategory === category
                  ? 'bg-primary-600 text-white'
                  : 'bg-white text-gray-600 hover:bg-gray-100'
              ]"
            >
              {{ category }}
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Post -->
    <section v-if="featuredPost" class="py-12 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-gradient-to-r from-primary-600 to-primary-800 rounded-2xl overflow-hidden text-white">
          <div class="grid md:grid-cols-2 gap-8">
            <div class="p-8 md:p-12">
              <div class="text-yellow-300 text-sm font-medium mb-2">Featured Story</div>
              <h2 class="text-3xl font-bold mb-4">{{ featuredPost.title }}</h2>
              <p class="text-gray-200 mb-6">{{ featuredPost.excerpt }}</p>
              <router-link 
                :to="`/blog/${featuredPost.slug}`"
                class="inline-flex items-center bg-yellow-400 text-gray-900 px-6 py-3 rounded-lg font-semibold hover:bg-yellow-300 transition-colors duration-200"
              >
                Read Full Story
                <svg class="ml-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                </svg>
              </router-link>
            </div>
            <div class="h-64 md:h-auto">
              <img :src="featuredPost.image" :alt="featuredPost.title" class="w-full h-full object-cover">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Blog Posts Grid -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div v-if="loading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
          <p class="mt-2 text-gray-600">Loading stories...</p>
        </div>

        <div v-else-if="filteredPosts.length === 0" class="text-center py-12">
          <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 12h6m-6-4h6m2 5.291A7.962 7.962 0 0112 15c-2.34 0-4.5-.904-6.131-2.38.164-.299.34-.597.541-.888A12.078 12.078 0 0112 9c2.467 0 4.751.75 6.64 2.037.205.291.381.59.535.896A7.962 7.962 0 0112 15z"></path>
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">No stories found</h3>
          <p class="mt-1 text-sm text-gray-500">Try adjusting your search or filter criteria.</p>
        </div>

        <div v-else class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <article 
            v-for="post in paginatedPosts" 
            :key="post.id" 
            class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-200"
          >
            <router-link :to="`/blog/${post.slug}`">
              <img :src="post.image" :alt="post.title" class="w-full h-48 object-cover">
            </router-link>
            <div class="p-6">
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm text-primary-600 font-medium">{{ post.category }}</span>
                <time class="text-sm text-gray-500">{{ formatDate(post.publishedAt) }}</time>
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-2">
                <router-link :to="`/blog/${post.slug}`" class="hover:text-primary-600 transition-colors duration-200">
                  {{ post.title }}
                </router-link>
              </h3>
              <p class="text-gray-600 mb-4">{{ post.excerpt }}</p>
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2">
                  <img 
                    src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=32&h=32&fit=crop&crop=face" 
                    alt="Author" 
                    class="w-8 h-8 rounded-full"
                  >
                  <span class="text-sm text-gray-700">{{ post.author }}</span>
                </div>
                <router-link 
                  :to="`/blog/${post.slug}`" 
                  class="text-primary-600 font-medium hover:text-primary-700 transition-colors duration-200"
                >
                  Read More →
                </router-link>
              </div>
            </div>
          </article>
        </div>

        <!-- Pagination -->
        <div v-if="totalPages > 1" class="mt-12 flex justify-center">
          <nav class="flex space-x-2">
            <button
              v-for="page in totalPages"
              :key="page"
              @click="currentPage = page"
              :class="[
                'px-4 py-2 rounded-lg text-sm font-medium transition-colors duration-200',
                currentPage === page
                  ? 'bg-primary-600 text-white'
                  : 'bg-white text-gray-600 hover:bg-gray-100'
              ]"
            >
              {{ page }}
            </button>
          </nav>
        </div>
      </div>
    </section>

    <!-- Newsletter CTA -->
    <section class="bg-primary-800 text-white py-16">
      <div class="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold mb-4">Never Miss a Story</h2>
        <p class="text-xl text-gray-200 mb-8">
          Get weekly insights and stories of transformation delivered directly to your inbox.
        </p>
        <form @submit.prevent="subscribeNewsletter" class="max-w-md mx-auto">
          <div class="flex">
            <input 
              v-model="newsletterEmail"
              type="email" 
              required
              placeholder="Enter your email" 
              class="flex-1 px-4 py-3 text-gray-900 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-yellow-400"
            >
            <button 
              type="submit" 
              class="px-6 py-3 bg-yellow-400 text-gray-900 rounded-r-lg font-semibold hover:bg-yellow-300 transition-colors duration-200"
            >
              Subscribe
            </button>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'


export default {
  name: 'Blog',
  setup() {
    
    const searchQuery = ref('')
    const selectedCategory = ref('All')
    const currentPage = ref(1)
    const postsPerPage = 9
    const newsletterEmail = ref('')

    const categories = ref([
      'All',
      'Personal Growth',
      'Reentry',
      'Social Justice',
      'Family',
      'Career',
      'Mental Health',
      'Community'
    ])

    // Mock blog posts - replace with API call
    const blogPosts = ref([
      {
        id: 1,
        title: "Finding Purpose After Prison",
        slug: "finding-purpose-after-prison",
        excerpt: "How I discovered my calling and built a meaningful life after serving four years in the Florida Department of Corrections.",
        content: "Full blog post content...",
        category: "Personal Growth",
        author: "Your Name",
        publishedAt: "2024-01-15",
        featured: true,
        image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop"
      },
      {
        id: 2,
        title: "The Power of Second Chances",
        slug: "power-of-second-chances",
        excerpt: "Why society needs to embrace redemption and how individuals can advocate for meaningful criminal justice reform.",
        category: "Social Justice",
        author: "Your Name",
        publishedAt: "2024-01-10",
        featured: false,
        image: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop"
      },
      {
        id: 3,
        title: "Building Your Support Network",
        slug: "building-support-network",
        excerpt: "Practical steps to find and nurture relationships that will sustain your growth and transformation journey.",
        category: "Community",
        author: "Your Name",
        publishedAt: "2024-01-05",
        featured: false,
        image: "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800&h=600&fit=crop"
      },
      {
        id: 4,
        title: "Navigating Job Interviews with a Record",
        slug: "job-interviews-with-record",
        excerpt: "Honest strategies for discussing your past during job interviews and landing meaningful employment.",
        category: "Career",
        author: "Your Name",
        publishedAt: "2024-01-01",
        featured: false,
        image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop"
      },
      {
        id: 5,
        title: "Healing Family Relationships",
        slug: "healing-family-relationships",
        excerpt: "How to rebuild trust and create healthy connections with family members after incarceration.",
        category: "Family",
        author: "Your Name",
        publishedAt: "2023-12-28",
        featured: false,
        image: "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=800&h=600&fit=crop"
      },
      {
        id: 6,
        title: "Managing Anxiety and PTSD",
        slug: "managing-anxiety-ptsd",
        excerpt: "Practical techniques for dealing with mental health challenges that often accompany reentry.",
        category: "Mental Health",
        author: "Your Name",
        publishedAt: "2023-12-25",
        featured: false,
        image: "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=800&h=600&fit=crop"
      }
    ])

    const loading = ref(false)

    const featuredPost = computed(() => 
      blogPosts.value.find(post => post.featured)
    )

    const filteredPosts = computed(() => {
      let posts = blogPosts.value.filter(post => !post.featured)
      
      // Filter by category
      if (selectedCategory.value !== 'All') {
        posts = posts.filter(post => post.category === selectedCategory.value)
      }
      
      // Filter by search query
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        posts = posts.filter(post => 
          post.title.toLowerCase().includes(query) ||
          post.excerpt.toLowerCase().includes(query) ||
          post.category.toLowerCase().includes(query)
        )
      }
      
      return posts
    })

    const totalPages = computed(() => 
      Math.ceil(filteredPosts.value.length / postsPerPage)
    )

    const paginatedPosts = computed(() => {
      const start = (currentPage.value - 1) * postsPerPage
      const end = start + postsPerPage
      return filteredPosts.value.slice(start, end)
    })

    const formatDate = (dateString) => {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(dateString).toLocaleDateString(undefined, options)
    }

    const subscribeNewsletter = () => {
      // Implement newsletter subscription logic
      console.log('Newsletter subscription:', newsletterEmail.value)
      newsletterEmail.value = ''
      // Show success message
    }

    onMounted(() => {
      // Load blog posts from API
      // store.dispatch('fetchBlogPosts')
    })

    return {
      searchQuery,
      selectedCategory,
      currentPage,
      newsletterEmail,
      categories,
      blogPosts,
      loading,
      featuredPost,
      filteredPosts,
      totalPages,
      paginatedPosts,
      formatDate,
      subscribeNewsletter
    }
  }
}
</script>
