package com.wararaki.sampleragapplication.repository

import com.wararaki.sampleragapplication.model.Passage
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository
import org.springframework.stereotype.Repository

@Repository
interface RAGRepository : ElasticsearchRepository<Passage, String> {
    fun findByContentContaining(content: String): List<Passage>
}
