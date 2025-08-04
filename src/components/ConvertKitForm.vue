<template>
  <div class="convertkit-form">
    <div v-if="!submitted" class="bg-white/10 backdrop-blur-sm rounded-lg p-6">
      <h3 class="text-xl font-semibold mb-3 text-white">Get Your Mental Freedom Guide</h3>
      <p class="text-gray-200 mb-4 text-sm">7 steps to reclaim your mental freedom, even in the toughest situations.</p>
      <form @submit.prevent="submitForm" class="flex flex-col sm:flex-row gap-2">
        <input 
          v-model="email"
          type="email" 
          placeholder="Enter your email" 
          required
          class="flex-1 px-4 py-2 rounded-lg text-gray-900 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        >
        <button 
          type="submit"
          :disabled="loading"
          class="bg-yellow-400 text-gray-900 px-6 py-2 rounded-lg font-semibold hover:bg-yellow-300 transition-colors duration-200 disabled:opacity-50"
        >
          {{ loading ? 'Sending...' : 'Get Free Guide' }}
        </button>
      </form>
    </div>
    
    <div v-else class="bg-green-50 border border-green-200 rounded-lg p-6">
      <div class="flex items-center">
        <svg class="w-5 h-5 text-green-400 mr-2" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
        </svg>
        <p class="text-green-800 font-medium">Thanks! Check your email for your Mental Freedom Guide.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'ConvertKitForm',
  props: {
    formId: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const email = ref('')
    const loading = ref(false)
    const submitted = ref(false)

    const submitForm = async () => {
      loading.value = true
      
      try {
        const response = await fetch(`https://api.convertkit.com/v3/forms/${props.formId}/subscribe`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            api_key: process.env.VUE_APP_CONVERTKIT_API_KEY,
            email: email.value
          })
        })

        if (response.ok) {
          submitted.value = true
          email.value = ''
        } else {
          alert('Something went wrong. Please try again.')
        }
      } catch (error) {
        console.error('Error:', error)
        alert('Something went wrong. Please try again.')
      } finally {
        loading.value = false
      }
    }

    return {
      email,
      loading,
      submitted,
      submitForm
    }
  }
}
</script>
