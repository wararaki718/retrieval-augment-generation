package com.wararaki.sampleragapplication.service

import com.wararaki.sampleragapplication.repository.RAGRepository
import org.springframework.stereotype.Service

@Service
class RAGService(private val repository: RAGRepository) {
    fun answer(content: String): String {
        // preprocess context
        // retrieval
        // build a prompt
        // generate
        return "text"
    }
}