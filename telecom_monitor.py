    # ========== 生成供手机读取的 usage.json ==========
    # summary['commonUse'] 和 summary['commonTotal'] 单位为 KB，需转换为 GB
    flow_used_gb = round(summary['commonUse'] / 1048576, 2)
    flow_total_gb = round(summary['commonTotal'] / 1048576, 2)
    flow_remaining_gb = round(flow_total_gb - flow_used_gb, 2)

    usage_json = {
        "balance": round(summary['balance'] / 100, 2),
        "flowUsed": flow_used_gb,
        "flowTotal": flow_total_gb,
        "voiceUsed": summary['voiceUsage'],
        "voiceTotal": summary['voiceTotal'] if summary['voiceTotal'] > 0 else 0,
        "updateTime": summary['createTime'],
        "statusIcon": status_icon
    }
    try:
        with open("usage.json", "w", encoding="utf-8") as f:
            json.dump(usage_json, f, ensure_ascii=False, indent=2)
        print(f"✅ 已生成 usage.json 文件，剩余流量: {flow_remaining_gb} GB")
    except Exception as e:
        print(f"⚠️ 生成 usage.json 失败: {e}")

    update_config()
