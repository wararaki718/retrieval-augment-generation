package com.wararaki.sampleragapplication

import com.wararaki.sampleragapplication.model.Passage
import com.wararaki.sampleragapplication.repository.RAGRepository
import org.springframework.boot.ApplicationRunner
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration

@Configuration
class RAGConfiguration {
    @Bean
    fun databaseInitializer(ragRepository: RAGRepository) = ApplicationRunner {
        val passage1 = Passage("sample1", "The capital of Japan is Tokyo.")
        ragRepository.save(passage1)

        val passage2 = Passage("sample2", "The capital of India is New Delhi.")
        ragRepository.save(passage2)
    }
}