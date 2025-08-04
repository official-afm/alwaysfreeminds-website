<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-primary-900 via-primary-800 to-primary-600 text-white py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-6">Let's Connect</h1>
        <p class="text-xl text-gray-200">
          Ready to start a conversation? I'd love to hear from you.
        </p>
      </div>
    </section>

    <!-- Contact Form Section -->
    <section class="py-16 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-2 gap-12">
          <!-- Contact Form -->
          <div>
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Send Me a Message</h2>
            <form @submit.prevent="submitForm" class="space-y-6">
              <!-- Name -->
              <div>
                <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
                  Full Name *
                </label>
                <input
                  id="name"
                  v-model="form.name"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-colors duration-200"
                  :class="{ 'border-red-500': errors.name }"
                >
                <p v-if="errors.name" class="mt-1 text-sm text-red-600">{{ errors.name }}</p>
              </div>

              <!-- Email -->
              <div>
                <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                  Email Address *
                </label>
                <input
                  id="email"
                  v-model="form.email"
                  type="email"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-colors duration-200"
                  :class="{ 'border-red-500': errors.email }"
                >
                <p v-if="errors.email" class="mt-1 text-sm text-red-600">{{ errors.email }}</p>
              </div>

              <!-- Subject -->
              <div>
                <label for="subject" class="block text-sm font-medium text-gray-700 mb-2">
                  Subject *
                </label>
                <select
                  id="subject"
                  v-model="form.subject"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-colors duration-200"
                  :class="{ 'border-red-500': errors.subject }"
                >
                  <option value="">Select a topic...</option>
                  <option value="consulting">Consulting Services</option>
                  <option value="speaking">Speaking Engagement</option>
                  <option value="collaboration">Collaboration Opportunity</option>
                  <option value="media">Media Interview</option>
                  <option value="support">General Support</option>
                  <option value="other">Other</option>
                </select>
                <p v-if="errors.subject" class="mt-1 text-sm text-red-600">{{ errors.subject }}</p>
              </div>

              <!-- Message -->
              <div>
                <label for="message" class="block text-sm font-medium text-gray-700 mb-2">
                  Message *
                </label>
                <textarea
                  id="message"
                  v-model="form.message"
                  required
                  rows="5"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-colors duration-200"
                  :class="{ 'border-red-500': errors.message }"
                  placeholder="Tell me about your situation, what you're looking for, or how I can help..."
                ></textarea>
                <p v-if="errors.message" class="mt-1 text-sm text-red-600">{{ errors.message }}</p>
              </div>

              <!-- Submit Button -->
              <button
                type="submit"
                :disabled="submitting"
                class="w-full bg-primary-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="submitting" class="flex items-center justify-center">
                  <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Sending...
                </span>
                <span v-else>Send Message</span>
              </button>

              <!-- Success Message -->
              <div v-if="submitted" class="p-4 bg-green-50 border border-green-200 rounded-lg">
                <div class="flex">
                  <svg class="w-5 h-5 text-green-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                  </svg>
                  <div class="ml-3">
                    <p class="text-sm text-green-700">
                      Thank you for your message! I'll get back to you within 24-48 hours.
                    </p>
                  </div>
                </div>
              </div>
            </form>
          </div>

          <!-- Contact Information -->
          <div>
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Other Ways to Connect</h2>
            
            <!-- Contact Cards -->
            <div class="space-y-6">
              <!-- Email -->
              <div class="bg-gray-50 p-6 rounded-lg">
                <div class="flex items-center space-x-3 mb-2">
                  <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                  </svg>
                  <h3 class="text-lg font-semibold text-gray-900">Email</h3>
                </div>
                <p class="text-gray-600 mb-2">For detailed inquiries and professional matters</p>
                <a href="mailto:contact@buymindinsights.com" class="text-primary-600 font-medium hover:text-primary-700">
                  contact@buymindinsights.com
                </a>
              </div>

              <!-- LinkedIn -->
              <div class="bg-gray-50 p-6 rounded-lg">
                <div class="flex items-center space-x-3 mb-2">
                  <svg class="w-6 h-6 text-primary-600" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                  </svg>
                  <h3 class="text-lg font-semibold text-gray-900">LinkedIn</h3>
                </div>
                <p class="text-gray-600 mb-2">Connect for professional networking and updates</p>
                <a href="#" class="text-primary-600 font-medium hover:text-primary-700">
                  Connect with me
                </a>
              </div>

              <!-- Response Time -->
              <div class="bg-primary-50 p-6 rounded-lg">
                <div class="flex items-center space-x-3 mb-2">
                  <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <h3 class="text-lg font-semibold text-gray-900">Response Time</h3>
                </div>
                <p class="text-gray-600">
                  I typically respond within 24-48 hours. For urgent matters, please mention 
                  it in your subject line.
                </p>
              </div>
            </div>

            <!-- FAQ Link -->
            <div class="mt-8 p-6 bg-gray-100 rounded-lg">
              <h3 class="text-lg font-semibold text-gray-900 mb-2">Frequently Asked Questions</h3>
              <p class="text-gray-600 mb-4">
                Before reaching out, you might find answers to common questions about consulting 
                services, speaking engagements, and collaboration opportunities.
              </p>
              <router-link to="/faq" class="text-primary-600 font-medium hover:text-primary-700">
                View FAQ →
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Trust Indicators -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-2xl font-bold text-gray-900 mb-8">Why People Trust BuyMindInsights</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="text-3xl font-bold text-primary-600 mb-2">100%</div>
            <div class="text-gray-600">Authentic experiences</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-primary-600 mb-2">24-48h</div>
            <div class="text-gray-600">Response time</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-primary-600 mb-2">4+ Years</div>
            <div class="text-gray-600">Lived experience</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'

export default {
  name: 'Contact',
  setup() {
    const form = reactive({
      name: '',
      email: '',
      subject: '',
      message: ''
    })

    const errors = reactive({})
    const submitting = ref(false)
    const submitted = ref(false)

    const validateForm = () => {
      const newErrors = {}

      if (!form.name.trim()) {
        newErrors.name = 'Name is required'
      }

      if (!form.email.trim()) {
        newErrors.email = 'Email is required'
      } else if (!/\S+@\S+\.\S+/.test(form.email)) {
        newErrors.email = 'Please enter a valid email'
      }

      if (!form.subject) {
        newErrors.subject = 'Please select a subject'
      }

      if (!form.message.trim()) {
        newErrors.message = 'Message is required'
      } else if (form.message.trim().length < 10) {
        newErrors.message = 'Please provide more details (at least 10 characters)'
      }

      Object.keys(errors).forEach(key => {
        delete errors[key]
      })
      Object.assign(errors, newErrors)

      return Object.keys(newErrors).length === 0
    }

    const submitForm = async () => {
      if (!validateForm()) {
        return
      }

      submitting.value = true

      try {
        // Replace with actual API call
        console.log('Form submission:', form)
        
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        submitted.value = true
        
        // Reset form
        Object.keys(form).forEach(key => {
          form[key] = ''
        })
        
        // Hide success message after 5 seconds
        setTimeout(() => {
          submitted.value = false
        }, 5000)
        
      } catch (error) {
        console.error('Form submission error:', error)
        // Handle error (show error message)
      } finally {
        submitting.value = false
      }
    }

    return {
      form,
      errors,
      submitting,
      submitted,
      submitForm
    }
  }
}
</script>